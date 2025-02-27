import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

ON_PROD = os.getenv('ON_PROD', 'False').strip().lower() == 'true'

# SECURITY WARNING:  don't run with debug turned on in production !
if ON_PROD:
    DEBUG = True
else:
    DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

# Application definition
INSTALLED_APPS = [
    'employees.apps.EmployeesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tlgrouptesttask.urls'

# Подключаю шаблоны
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tlgrouptesttask.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#         'default': {
#             'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
#             'NAME': os.getenv('DB_NAME', 'django'),
#             'USER': os.getenv('POSTGRES_USER', 'django'),
#             'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
#             'HOST': os.getenv('DB_HOST'),
#             'PORT': os.getenv('DB_PORT')
#         }
#     }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

# Путь к статическим файлам
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Папка статических файлов
STATICFILES_DIRS = [os.path.join(BASE_DIR, '_inspinia')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
