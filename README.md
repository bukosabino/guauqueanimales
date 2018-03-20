# Guau! qué animales

Web Server and API Web for lost/found/adoption/reception animals

Run example (in spanish) -> http://guauqueanimales.com



## Local settings:

set settings values in encuentra_perros_server/settings_local.py

TO_ADMIN_EMAIL = ('example@gmail.com',)

FROM_ADMIN_EMAIL = ['example1@gmail.com', 'example2@gmail.com',]

SECRET_KEY = 'key_example'



## Twitter settings:

for send tweets, guauqueanimales uses this python wrapper API Twitter: https://github.com/ryanmcgrath/twython

from twython import Twython

CONSUMER_KEY = ''

CONSUMER_SECRET = ''

ACCESS_TOKEN = ''

ACCESS_TOKEN_SECRET = ''

TWITTER = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)



## Deploy local:

* git clone https://github.com/bukosabino/guauqueanimales.git
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver
