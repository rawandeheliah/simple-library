from settings.base import *

DEBUG = False

import django_heroku
django_heroku.settings(locals())