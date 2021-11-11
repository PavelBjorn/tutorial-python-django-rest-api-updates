import datetime as datetime
from django.conf import settings
from django.utils import timezone
from rest_framework_jwt.settings import api_settings

expier_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

def jwt_response_payload_handler(token, user: None, request=None):
    return {
        'token': token,
        'user': user.id,
        'expires': timezone.now() + expier_delta - datetime.timedelta(seconds=200)
    }

def get_expires():
    return timezone.now() + expier_delta - datetime.timedelta(seconds=200)