"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^2r_7(vr#efuy5=k_$0pk0)s8wi8gi0v7^x4yj1hm$e1q8rm99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',
    'ckeditor',
    'ckeditor_uploader',
    'autopep8',
    'tinymce',
    'mptt',
    'fontawesomefree'

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

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notobo_blogs',
        'USER': 'notobo_blogs',
        'PASSWORD': 'notobo_blogs',
        'HOST': '103.101.163.106',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci;'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'server/static/'


if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'server/static')
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'server/static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#     },
# }
CKEDITOR_UPLOAD_PATH = 'uploads/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'extraPlugins': 'codesnippet',
#         'toolbar': 'full',
#     },
# }
CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'bootstrapck',
        'skin': 'moono',
        'toolbar': 'full',
        'codeSnippet_theme': 'monokai',
        'extraPlugins': ','.join(
            [
                # add the follow plugins
                'codesnippet',
                # 'widget',
                # 'dialog',
            ]),
    },
    'commment': {
        'toolbar': 'Custom',
        # 'skin': 'moono',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['CodeSnippet'],
        ],
        'codeSnippet_theme': 'monokai',
        'extraPlugins': ','.join(
            [
                # add the follow plugins
                'codesnippet',
                "emoji"

            ]),
    },
}


# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
# TINYMCE_DEFAULT_CONFIG = {
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'silver',
#     'plugins': '''
#             textcolor save link image media preview codesample contextmenu
#             table code lists fullscreen  insertdatetime  nonbreaking
#             contextmenu directionality searchreplace wordcount visualblocks
#             visualchars code fullscreen autolink lists  charmap print  hr
#             anchor pagebreak
#             ''',
#     'toolbar1': '''
#             fullscreen preview bold italic underline | fontselect,
#             fontsizeselect  | forecolor backcolor | alignleft alignright |
#             aligncenter alignjustify | indent outdent | bullist numlist table |
#             | link image media | codesample |
#             ''',
#     'toolbar2': '''
#             visualblocks visualchars |
#             charmap hr pagebreak nonbreaking anchor |  code |
#             ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True
