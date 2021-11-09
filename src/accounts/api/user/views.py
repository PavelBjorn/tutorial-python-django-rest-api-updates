from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserDetailSerializer

User = get_user_model()


class UseDetailApiView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'
