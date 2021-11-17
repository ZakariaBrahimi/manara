from manara.settings.common import *
import os
# import environ

# env = environ.Env()
# environ.Env.read_env()
DEBUG = False
ALLOWED_HOSTS = []

SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: update this when you have the production host
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
# 5


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")