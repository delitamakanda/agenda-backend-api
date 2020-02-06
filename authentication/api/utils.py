import datetime
from django.conf import settings
from django.utils import timezone

expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


def jwt_response_payload_handler(token, request=None):
    return {
        'token': token,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200),
    }