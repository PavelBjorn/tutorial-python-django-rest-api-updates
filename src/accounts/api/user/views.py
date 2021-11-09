from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserDetailSerializer
from status.models import Status

from status.api.serializers import StatusInlineUserSerializer
from accounts.api.permissions import AnonPermissionOnly

User = get_user_model()


class UserDetailApiView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusApiView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
