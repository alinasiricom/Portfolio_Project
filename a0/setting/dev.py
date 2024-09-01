from a0.settings import *

SECRET_KEY = 'django-insecure-d7+ofdmkfxg)=z4&ek**paql6q2_2av2veg5t)b32@6)8st9@k'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
