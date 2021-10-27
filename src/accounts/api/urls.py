from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from .views import AuthView

urlpatterns = [
    url(r'^$', AuthView.as_view()),
    url(r'jwt/$', obtain_jwt_token),
    url(r'jwt/refresh/$', refresh_jwt_token),
]
