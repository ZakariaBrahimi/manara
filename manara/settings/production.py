from manara.settings.common import *
import environ

env = environ.Env()
environ.Env.read_env()
DEBUG = False

SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: update this when you have the production host
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost']