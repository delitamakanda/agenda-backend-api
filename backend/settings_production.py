from backend.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['*']

DEBUG = os.environ.get('DEBUG')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SERVER_EMAIL = os.environ.get('ADMIN_EMAIL')
ADMIN_NAME = os.environ.get('ADMIN_NAME')

ADMINS = (
    (ADMIN_NAME, SERVER_EMAIL),
)

SEND_BROKEN_LINK_EMAILS=True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get('SENDGRID_SERVER')
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = os.environ.get('SENDGRID_PORT')
EMAIL_USE_TLS = True


# cors

CORS_REPLACE_HTTPS_REFERER = True

