from settings.base import *
import django_heroku

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'catalog.storage_backends.MediaStorage'

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True


django_heroku.settings(locals())
