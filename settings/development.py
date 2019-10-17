from settings.base import *

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'catalog.storage_backends.MediaStorage'

ALLOWED_HOSTS = ['still-tundra-14682.herokuapp.com']
DEBUG = False

