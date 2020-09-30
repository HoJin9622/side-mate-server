import os

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'sidemate.ciqfc7ucqysg.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'sidemate123',
    }
}

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_URL = 'http://127.0.0.1:8000/media/'
# MEDIA_URL = 'http://13.124.252.168:8000/media/'
MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media/')

