# test_statistics

##### Иструкция по запуску на локальной машине:
- git clone https://github.com/Hawool/tinder.git
- cd tinder
- docker build -t tinder_img .
- docker run --rm --name tinder_container -p 8000:8000 tinder_img

Затем можно открыть в браузере http://0.0.0.0:8000

Фильтрация реализована с помощью django-filter, get запрос со всеми фильтрами: http://127.0.0.1:8000/api/v1/statistic/?views__lte=&views__gte=&clicks__lte=&clicks__gte=&cost__lte=&cost__gte=&date__lte=&date__gte=

### Методы
Метод создания:
POST http://127.0.0.1:8000/api/v1/statistic/

{
        "date": "2021-11-17",
        "views": 12,
        "clicks": 23,
        "cost": "400.89"
    },

Метод обновления данных:
PUT/PATCH http://127.0.0.1:8000/api/v1/statistic/{id}
{
        "date": "2021-11-17",
        "views": 12000,
        "clicks": 23000,
        "cost": "400.89"
    },

Метод удаления:
DELETE http://127.0.0.1:8000/api/v1/statistic/{id}

Метод просмотра всех:
GET http://127.0.0.1:8000/api/v1/statistic/