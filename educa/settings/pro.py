from .base import *

DEBUG = False

ADMINS = (
    ('Deepankumar', 'deepankumar@testpress.in'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '!@#$%^&*',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True