from settings.base import *
import django_heroku


DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True


django_heroku.settings(locals())
