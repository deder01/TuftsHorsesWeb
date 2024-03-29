# Django settings for tuftshorses project.
import os
import dj_database_url
from re import compile

LOGIN_URL = '/login/'

LOGIN_EXEMPT_URLS = (
 r'^static/',
 r'^about\.html$',
 r'^legal/', # allow any URL under /legal/*
 r'^invitation/\w+',
 r'^register/',
 r'^api/',
 r'^forgotpassword/',
)

import middleware


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/tuftshorses')}

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

PROJECT_ROOT_PATH=(os.path.dirname(os.path.realpath(__name__)))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH,"static/")
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = os.getenv('STATIC_URL', 'http://s3.amazonaws.com/tuftshorses/')

# Additional locations of static files
STATICFILES_DIRS = (
    #os.path.join(PROJECT_ROOT_PATH,"static/"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJ537AK2N3U6TOO4Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'tuftshorses'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME')
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')

ROOT_URL = os.getenv('ROOT_URL','localhost:5000')


# Make this unique, and don't share it with anybody.
SECRET_KEY = '8wmk99)&amp;dyuh%^0gm#ad%859)@r-)b*6*-@8x=^wf)-hgurh@h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'djaml.loaders.DjamlFilesystemLoader',
    'djaml.loaders.DjamlAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'middleware.LoginRequiredMiddleware',
    'middleware.XsSharing',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tuftshorses.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tuftshorses.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, "templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'horseshow',
    'tastypie',
    'south',
    'invitations',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


