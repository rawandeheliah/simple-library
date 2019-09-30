from settings.base import *
import django_heroku

ALLOWED_HOSTS = ['.herokuapp.com']
DEBUG = False


django_heroku.settings(locals())