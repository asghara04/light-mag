from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '. }rA\ `Uv @a@ v:GTT`u7w=rxZrUl$h{#T[`SzZmU,2BOq0+DlL@>8|H1G`%t)5OSzf~i9f\    dYj?j?0.WBm$N"dJI1?=^Ya.<23Zk5?b#AHb7Nq!*O+aA%   o$seG:jsmP>.!z{\'sXBKK<`]w0gX$-3_yfP3d`k^Q2i@=psT<L6X~mr$%V1LTG,jUt#H5~r,~TU~"]KA|c1pa/"H:z"+QK{Dlwsq_}F-\']@KzO&Zz+9bxb;p8#?OTi<&+zX9I=bOGns_^}w%T>woo}Am8=|iIUT29>|Gx6)Rw`Go3\jFMU2$\'n[HWJKF+h]BO=]o%/,&-2?6~lH9`X8=\'1!|&k^t.96~VO7GIZ4s|h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'rest_framework',
    'image',
    'category',
    'user',
    'tag',
    'article',
    'comment',
    'corsheaders',
    'rest_framework_jwt',
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
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://light-mag.ir:8080",
    "http://admin.light-mag.ir:8080",
    "http://localhost:8100",
    "http://127.0.0.1:8100"
]

ROOT_URLCONF = 'lightmag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lightmag.wsgi.application'

AUTH_USER_MODEL = "user.User"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "user.permissions.IsAdminOrReadOnly",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_RENDERER_CLASSES":(
        "rest_framework.renderers.JSONRenderer",
    )
}


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lightmagdb',
        'USER': 'asghara04',
        'PASSWORD': 'asghara04 a20041383',
        'HOST': '127.0.0.1',
        'PORT': "3306",
        'OPTIONS': {
            'use_unicode': True,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=2),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'