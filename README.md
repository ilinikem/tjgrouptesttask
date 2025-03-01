# TLGroup Test Task

## Описание
Тестовое задание для компании TLGroup. Django-приложение выводит на главной странице подразделения и сотрудников в таблице.

## Установка и запуск

### 1. Клонирование репозитория
```sh
git clone https://github.com/ilinikem/tjgrouptesttask.git
cd tjgrouptesttask
```

### 2. Создание виртуального окружения и установка зависимостей
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Применение миграций и запуск сервера
```sh
python manage.py migrate
python manage.py runserver
```

### 4. Создание тестовых данных
```sh
python manage.py make_test_data
```

## Тестирование

Запуск тестов выполняется командой:
```sh
python manage.py test
```

## Базы данных

По умолчанию использована sqlite3, можно подключить postgresql, просто изменив настройки в файле settings.py

## Настройка переменных окружения
Секретные данные необходимо хранить в файле `.env`. Создайте его в корневой папке проекта и укажите необходимые переменные.

```
Пример:
SECRET_KEY=django-insecure-dsfby47r3hfy43372h32dh38d823d32e23
ON_PROD=False

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
DB_HOST=db
DB_PORT=5432
```