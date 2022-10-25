import sys

try:
    from settings.base import *
except ImportError as e:
    sys.stdout.write('Cannot import settings.base\n')
    sys.exit(0)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
