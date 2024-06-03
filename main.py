import json

from flask import Flask, jsonify, request

from Twit.model.twit import Twit

twits = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'id': obj.id, 'body': obj.body, 'author': obj.author}
        return super().default(obj)

@app.route('/twit', methods=['POST'])
def create_twit():
    '''  {"id": 1, 'body': 'Hello World', 'author': '@aqaguy'}  '''
    twit_json = request.get_json()
    twit = Twit(twit_json['id'], twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twit():
    serialized_twits = [twit.to_dict() for twit in twits]
    return jsonify({'twits': serialized_twits})


@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id):
    twit_json = request.get_json()
    for twit in twits:
        if twit.id == twit_id:
            twit.body = twit_json.get('body', twit.body)
            twit.author = twit_json.get('author', twit.author)
            return jsonify({'status': 'success'})
    return jsonify({'error': 'Twit not found'})


@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit(twit_id):
    for twit in twits:
        if twit.id == twit_id:
            twits.remove(twit)
            return jsonify({'status': 'success'})
    return jsonify({'error': 'Twit not found'})


if __name__ == '__main__':
    app.run(debug=True)
