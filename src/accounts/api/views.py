from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_jwt.settings import api_settings
from django.db.models import Q

from .serializers import UserRegisterSerailizer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_respose_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class AuthAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': "Already authenticated!"}, status=400)

        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                print(user)
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                respones = jwt_respose_payload_handler(token, user, request=request)
                return Response(respones)
        return Response({'detail': 'Invalida credentials'}, status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerailizer
    permission_classes = [permissions.AllowAny]

# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response({'detail': "Already registred and are authenticated!"}, status=400)
#
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#
#         qs = User.objects.filter(
#             Q(username__iexact=username) |
#             Q(email__iexact=username)
#         )
#
#         if password != password2:
#             return Response({"password": "Password must match."}, status=401)
#         if qs.exists():
#             return Response({"detail": "This user already exists"}, status=401)
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(raw_password=password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             respones = jwt_respose_payload_handler(token, user, request=request)
#             return Response(respones, status=201)
#
#         return Response({'detail': 'Invalida Request'}, status=401)
