from .common import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PASSWORD_VALIDATORS = []

# Those settings are used to generate absolute urls
PROTOCOL = 'http'
SITE_URL = 'localhost:8000'
