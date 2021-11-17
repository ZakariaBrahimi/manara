from manara.settings.common import *

DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "stark-escarpment-63219.herokuapp.com", "127.0.0.1"]

SECRET_KEY = 'django-insecure-j6$pc8m8knv0(mbwwj*=cw@uz4bnov)4e@5r1#n4_w4di9cmm9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
]