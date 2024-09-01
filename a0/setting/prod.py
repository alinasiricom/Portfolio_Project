from a0.settings import *


SECRET_KEY = 'django-insecure-d7+ofdmkfxg)=z4&ek**paql6q2_2av2veg5t)b32@6)8st9@k'

DEBUG = False

CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['alinasiri.com', 'www.alinasiri.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = '/home/alinasir/public_html/static'
MEDIA_ROOT = '/home/alinasir/public_html/media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

