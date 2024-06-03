# Краткая инструкция по запуску 

## 1. Клонируйте репозиторий

`git clone https://github.com/PrimeLebedev/Twit.git`

## 2. Установите необходимые зависимости

`pip install -r requirements.txt`

## 3. Запустите Flask-приложение

`python main.py`

## 4. Доступ к API
После запуска приложения вы сможете обращаться к вашему API по URL: http://localhost:5000/

## 5. Тестирование API
Вы можете использовать инструменты для тестирования API, например, Postman, чтобы отправлять запросы на ваш сервер и проверять его функциональность.

## 6. Примеры запросов

### Создание Twit

Метод: POST

URL: /twit

Пример запроса:

`http://localhost:5000/twit`

Пример тела запроса:

```json
{
    "id": 1,
    "body": "Hello, Twit",
    "author": "@aqaguy"
}
```
Ответ:

```json
{
    "status": "succsess"
}
```

### Чтение Twit

Метод: GET

URL: /twit

Пример запроса:

`http://localhost:5000/twit`

Ответ:

```json
{
    "twits": [
        {
            "author": "@aqaguy",
            "body": "Hello, Twit",
            "id": 1
        }
    ]
}
```

### Обновление Twit

Метод: PUT

URL: /twit/<int:twit_id>

Пример запроса:

`http://localhost:5000/twit/1`

Пример тела запроса:

```json
{
    "id": 1,
    "body": "Updated Twit",
    "author": "@aqaguy"
}
```
Ответ:

```json
{
    "status": "success"
}
```

### Удаление Twit

Метод: DELETE

URL: /twit/<int:twit_id>

Пример запроса:

`http://localhost:5000/twit/1`

Ответ:

```json
{
    "status": "success"
}
```
