# Social network

## Работа с проектом
# Надо запустить postgres server
## Создать базу данных с данными файла настроек
```
DB_NAME=portal
DB_USER=portal
DB_PASSWORD=7xDeHViUt4mG0tjv
DB_HOST=localhost
DB_PORT=5432
```
# Запуск виртуального окружения
```
python3 -m venv env
source env/bin/activate
```
# Установка библиотек
```
pip install -r requirements.txt
```
# Запуск миграции
```
python manage.py makemigrations
python manage.py migrate
```
# Запуск проекта
```
python manage.py runserver
```
# Все api в swagger по пути
```
http://127.0.0.1:8000/swagger/
```
