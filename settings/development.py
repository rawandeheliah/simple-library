from settings.base import *


def populate_hosts():
    hosts = os.environ.get('ALLOWED_HOSTS')
    hosts_list = []
    for host in hosts.split(','):
        hosts_list.append(host)
    return hosts_list


ALLOWED_HOSTS = populate_hosts()
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'catalog.storage_backends.MediaStorage'

DEBUG = False
