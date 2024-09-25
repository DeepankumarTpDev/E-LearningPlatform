from .base import *

DEBUG = False

ADMINS = (
    ('Deepankumar', 'deepankumar@testpress.in'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '!@#$%^&*',
    }
}