from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from .views import UserDetailApiView, UserStatusApiView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailApiView.as_view(), name='detail'),
    url(r'^(?P<username>\w+)/status/$', UserStatusApiView.as_view(), name='status-list')
]
