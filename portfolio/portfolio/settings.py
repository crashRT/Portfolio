from pathlib import Path
import os
import environ
from .local_settings import *


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = env('SECRET_KEY')
# ↑別ファイルに移したので削除

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOSTS = ['portfolio-335223.an.r.appspot.com',
                 'localhost', 'crashrt.work', 'www.crashrt.work']

#DEBUG = False
#ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'top.apps.TopConfig',
    'picture.apps.PictureConfig',
    'movie.apps.MovieConfig',
    'modeling.apps.ModelingConfig',
    'note.apps.NoteConfig',
    'others.apps.OthersConfig',
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

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# GAE本番環境
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/{}'.format(env('DB_HOST')),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'NAME': env('DB_NAME'),
    }
}


# 開発環境
# 事前に./cloud_sql_proxyを実行してプロキシ経由でアクセスできるようにする必要がある。
#     DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# DATABASES = {
#        'default': {
# 'ENGINE': 'django.db.backends.mysql',
#            'HOST': '127.0.0.1',
# 'PORT': '3306',
#            'USER': '[YOUR-USERNAME]',
#            'PASSWORD': '[YOUR-PASSWORD]',
#            'NAME': '[YOUR-DATABASE]',
#        }
#    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
