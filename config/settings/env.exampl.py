from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: don't run with allowed host all in production!
ALLOWED_HOSTS = ['*']

BACKEND_URL = "http://127.0.0.1:8000/"

INSTALLED_APPS += [
    'rest_framework_swagger',
]

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
    'rest_framework.authentication.SessionAuthentication'  # do not use this on production
)

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '#DATABASE_NAME',
        'USER': '#USER_WITH_PERMISSION_TO_DATABASE',
        'PASSWORD': '#USER_PASSWORD',
        'HOST': '127.0.0.1',
        'PORT': 5432,
       }
}

# Smtp server  setting for email verification
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '#HOST_USER_EMAIL'
EMAIL_HOST_PASSWORD = '#HOST_USER_PASSWORD'
EMAIL_PORT = 587

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static')
]
APPLICANTS_VIEW_TOKEN = ''
