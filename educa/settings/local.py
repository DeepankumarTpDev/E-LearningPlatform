from .base import*

DEBUG = True

DATABASE = {
    'default':{
        'Engine': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}