from backend.settings import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = config('DEBUG', cast=bool)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ADMINS = (
    ('Délita', 'delita.makanda@gmail.com'),
)

SEND_BROKEN_LINK_EMAILS=True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')

SERVER_EMAIL = config('SERVER_EMAIL')

