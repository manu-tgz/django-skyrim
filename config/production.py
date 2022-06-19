from config.settings import *
import dj_database_url
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# # Database
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
