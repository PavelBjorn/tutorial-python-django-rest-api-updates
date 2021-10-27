import datetime as datetime
from django.conf import settings
from django.utils import timezone

expier_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token, user: None, reqeust=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expier_delta - datetime.timedelta(seconds=200)
    }
