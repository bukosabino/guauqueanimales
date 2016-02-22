# Guau! qué animales

Web Server and API Web for lost/found/adoption/reception animals

Run example (in spanish) -> http://guauqueanimales.com



## Local settings:

set settings values in encuentra_perros_server/settings_local.py

TO_ADMIN_EMAIL = ('example@gmail.com',)
FROM_ADMIN_EMAIL = ['example1@gmail.com', 'example2@gmail.com',]
SECRET_KEY = 'key_example'

for send tweets, i use this python wrapper API Twitter: https://github.com/ryanmcgrath/twython

from twython import Twython
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
TWITTER = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



## Local set up:

$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
