from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from .views import UseDetailApiView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UseDetailApiView.as_view(), name='detail')
]
