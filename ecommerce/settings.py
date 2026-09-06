from pathlib import Path
import os
import dj_database_url


# ==================================================
# BASE DIRECTORY
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# SECURITY
# ==================================================

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-development-key'
)

# Local computer  -> DEBUG = True
# Render          -> DEBUG = False
DEBUG = os.environ.get('RENDER', '') != 'true'


ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# Render automatically provides its hostname
RENDER_EXTERNAL_HOSTNAME = os.environ.get(
    'RENDER_EXTERNAL_HOSTNAME'
)

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ==================================================
# INSTALLED APPLICATIONS
# ==================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ShopSphere app
    'store',
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise must come immediately after
    # SecurityMiddleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==================================================
# URL CONFIGURATION
# ==================================================

ROOT_URLCONF = 'ecommerce.urls'


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Makes {{ cart }} available on every page
                'store.context_processors.cart',
            ],
        },
    },
]


# ==================================================
# WSGI
# ==================================================

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# ==================================================
# DATABASE
# ==================================================

# On Render:
# DATABASE_URL exists -> PostgreSQL
#
# Locally:
# DATABASE_URL doesn't exist -> SQLite

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ==================================================
# PASSWORD VALIDATION
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


# ==================================================
# INTERNATIONALIZATION
# ==================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ==================================================
# STATIC FILES
# ==================================================

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


# These are the six fixed product images used by the
# internship demo.
#
# collectstatic copies:
#
# media/products/...
#
# to:
#
# staticfiles/media/products/...
#
# WhiteNoise can then serve them on Render.

STATICFILES_DIRS = [
    ('media', BASE_DIR / 'media'),
]


# ==================================================
# MEDIA FILES
# ==================================================

MEDIA_ROOT = BASE_DIR / 'media'


# IMPORTANT:
#
# Local development:
#   /media/products/...
#   Django runserver serves these files.
#
# Render production:
#   /static/media/products/...
#   WhiteNoise serves the collected copies.
#
# Keeping these different prevents the error:
#
# "runserver can't serve media if MEDIA_URL
#  is within STATIC_URL"

if DEBUG:
    MEDIA_URL = '/media/'
else:
    MEDIA_URL = '/static/media/'


# ==================================================
# STORAGE
# ==================================================

STORAGES = {
    # Required for Product.image / ImageField
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },

    # WhiteNoise production static storage
    'staticfiles': {
        'BACKEND': (
            'whitenoise.storage.'
            'CompressedManifestStaticFilesStorage'
        ),
    },
}


# ==================================================
# DEFAULT PRIMARY KEY
# ==================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==================================================
# AUTHENTICATION
# ==================================================

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'