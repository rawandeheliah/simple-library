from settings.base import *
import django_heroku


ALLOWED_HOSTS = ['https://still-tundra-14682.herokuapp.com']
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'catalog.storage_backends.MediaStorage'
django_heroku.settings(locals())
