# Minio-API

| Endpoint       | Parameters                                 |
|----------------|--------------------------------------------|
| GET /frames    | **request body** <br> *request_id*: string |
| DELETE /frames | **request body** <br> *request_id*: string |
| POST /frames   | **form data** <br> files: binary           |

### Развертывание на docker
Для развертывания используйте: `docker-compose -f docker-compose.yml up`

### Тесты на docker
Для тестирования используйте: `docker-compose -f docker-compose-test.yml up`

### Локальный запуск
Для локального запуска используйте: `main.py`

### Локальное тестирование
Для локального тестирования используйте: `pytest`


### Версии

*fastapi version 0.78.0*

*minio version 7.1.9*

*Docker version 20.10.14*

*docker-compose version 2.4.1*

*SQLAlchemy version 1.4.37*

*Python 3.10.2*
