import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# LOCAL settings
TO_ADMIN_EMAIL = ('example1@gmail.com',)
FROM_ADMIN_EMAIL = ['example2@gmail.com', 'example3@gmail.com',]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR + '/media/'

MEDIA_URL = '/media/'

# Documentation: https://github.com/ryanmcgrath/twython
from twython import Twython
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
TWITTER = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
