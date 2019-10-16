from settings.base import *
import django_heroku

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'catalog.storage_backends.MediaStorage'

ALLOWED_HOSTS = ['still-tundra-14682.herokuapp.com']
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True


django_heroku.settings(locals())
