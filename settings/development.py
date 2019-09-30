from settings.base import *
import django_heroku

ALLOWED_HOSTS = ['https://still-tundra-14682.herokuapp.com']
DEBUG = True


django_heroku.settings(locals())