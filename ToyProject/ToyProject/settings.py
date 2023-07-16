"""
Django settings for ToyProject project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from .secret_manager import get_secret


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ToyProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [f'{BASE_DIR}/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ToyProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# MySQL 사용을 위한 설정
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql' ,
#         'HOST': 'localhost' ,
#         'PORT': '3306',
#         'NAME': 'mydb',
#         'USER': 'root',
#         'PASSWORD': '',
#     },
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / "static",
        ]
else:
    STATIC_ROOT = BASE_DIR / "static_root"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




#for user pw rest email service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 메일을 호스트하는 서버
EMAIL_HOST = 'smtp.gmail.com'

# mail과의 통신하는 포트
EMAIL_PORT = '587'

# 발신할 이메일
# EMAIL_HOST_USER = '아이디@mail.com'
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
# 발신할 메일의 비밀번호
# EMAIL_HOST_PASSWORD = '비밀번호'
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
# TLS 보안 방법
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 세션 만료 기간, 단위 : 초(sec)
# ref : docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SESSION_COOKIE_AGE
SESSION_COOKIE_AGE = 3600
# 웹브라우저 종료시 로그인 세션 종료
# ref : docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SESSION_EXPIRE_AT_BROWSER_CLOSE
# 크롬과 같은 브라우저에서는 본 기능을 막는 기능이 있으므로 세션 만료기간을 1시간으로 설정하였음
# remember me 기능 활성화를 위해서 False로 변경
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Request가 발생시 세션이 자동으로 연장됨. Request가 많이 발생하는 홈페이지에서는 DB 부담으로 인해 권장하지 않는 것으로 보인다.
SESSION_SAVE_EVERY_REQUEST = False

# 비밀번호 찾기 페이지 만료시간, 단위 : 초(sec)
PASSWORD_RESET_TIMEOUT = 86400