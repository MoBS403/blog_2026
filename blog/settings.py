# """
# Django settings for blog project.
# Compatible with Django 5.2+
# """

# import os
# from pathlib import Path
# from django.contrib.messages import constants

# # --------------------------------------------------
# # BASE DIR
# # --------------------------------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent

# # --------------------------------------------------
# # SECURITY
# # --------------------------------------------------
# SECRET_KEY = 'troque-essa-chave-em-producao'

# DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# # --------------------------------------------------
# # APPLICATIONS
# # --------------------------------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# INSTALLED_APPS = [
#     # Apps do projeto
#     'posts',
#     'categorias',
#     'comentarios',

#     # Django core
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.humanize',

#     # Terceiros
#     'crispy_forms',
#     'crispy_bootstrap4',
#     'axes',
#     'django_summernote',
# ]

# # --------------------------------------------------
# # MIDDLEWARE
# # --------------------------------------------------
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',

#     # Django Axes
#     'axes.middleware.AxesMiddleware',
# ]

# # --------------------------------------------------
# # URL / WSGI
# # --------------------------------------------------
# ROOT_URLCONF = 'blog.urls'
# WSGI_APPLICATION = 'blog.wsgi.application'

# # --------------------------------------------------
# # TEMPLATES
# # --------------------------------------------------
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# # --------------------------------------------------
# # DATABASE (MySQL)
# # --------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'blog_db',
#         'USER': 'root',
#         'PASSWORD': 'eu sei ,, vai toma cú kkk ',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }



# # --------------------------------------------------
# # PASSWORD VALIDATION
# # --------------------------------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # --------------------------------------------------
# # INTERNATIONALIZATION
# # --------------------------------------------------
# LANGUAGE_CODE = 'pt-BR'
# TIME_ZONE = 'America/Sao_Paulo'

# USE_I18N = True
# USE_TZ = True

# # --------------------------------------------------
# # STATIC & MEDIA
# # --------------------------------------------------
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'templates/static']
# STATIC_ROOT = BASE_DIR / 'static'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # --------------------------------------------------
# # MESSAGES (Bootstrap)
# # --------------------------------------------------
# MESSAGE_TAGS = {
#     constants.ERROR: 'alert-danger',
#     constants.WARNING: 'alert-warning',
#     constants.SUCCESS: 'alert-success',
#     constants.INFO: 'alert-info',
# }

# # --------------------------------------------------
# # CRISPY FORMS
# # --------------------------------------------------
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
# CRISPY_TEMPLATE_PACK = "bootstrap4"

# # --------------------------------------------------
# # DJANGO AXES
# # --------------------------------------------------
# AUTHENTICATION_BACKENDS = [
#     'axes.backends.AxesBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]

# AXES_FAILURE_LIMIT = 3
# AXES_COOLOFF_TIME = None
# AXES_LOCK_OUT_AT_FAILURE = True


# # --------------------------------------------------
# # SECURITY (DESENVOLVIMENTO)
# # --------------------------------------------------
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # ⚠️ EM DEV → False
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False

# # --------------------------------------------------
# # DEFAULT LOGIN
# # --------------------------------------------------
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

# # --------------------------------------------------
# # LOCAL SETTINGS (opcional)
# # --------------------------------------------------
# try:
#     from .local_settings import *
# except ImportError:
#     pass





"""
Django settings for blog project.
Production-ready for Render + PostgreSQL
"""

import os
from pathlib import Path
from django.contrib.messages import constants
import dj_database_url

# --------------------------------------------------
# BASE DIR
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    # Apps do projeto
    "posts",
    "categorias",
    "comentarios",

    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # Terceiros
    "crispy_forms",
    "crispy_bootstrap4",
    "axes",
    "django_summernote",
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Static no Render
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Django Axes
    "axes.middleware.AxesMiddleware",
]

# --------------------------------------------------
# URL / WSGI
# --------------------------------------------------
ROOT_URLCONF = "blog.urls"
WSGI_APPLICATION = "blog.wsgi.application"

# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# --------------------------------------------------
# DATABASE (Render PostgreSQL)
# --------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3",
        conn_max_age=600,
        ssl_require=True,
    )
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = "pt-BR"
TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC & MEDIA
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# MESSAGES (Bootstrap)
# --------------------------------------------------
MESSAGE_TAGS = {
    constants.ERROR: "alert-danger",
    constants.WARNING: "alert-warning",
    constants.SUCCESS: "alert-success",
    constants.INFO: "alert-info",
}

# --------------------------------------------------
# CRISPY FORMS
# --------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# --------------------------------------------------
# DJANGO AXES
# --------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AXES_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = None
AXES_LOCK_OUT_AT_FAILURE = True

# --------------------------------------------------
# SECURITY (RENDER)
# --------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = not DEBUG

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# --------------------------------------------------
# LOGIN
# --------------------------------------------------
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# --------------------------------------------------
# LOGGING (Render-friendly)
# --------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# --------------------------------------------------
# LOCAL SETTINGS (opcional)
# --------------------------------------------------
try:
    from .local_settings import *
except ImportError:
    pass


