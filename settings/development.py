from settings.base import *
import django_heroku

ALLOWED_HOSTS = ['https://still-tundra-14682.herokuapp.com']
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True


django_heroku.settings(locals())
