from django.conf.urls import url

from .views import (
    UpdateModelDetailAPI,
    UpdateModelListAPI
)

urlpatterns = [
    url(r'^$', UpdateModelListAPI.as_view()),
    url(r'(?P<update_id>\d+)/$', UpdateModelDetailAPI.as_view())
]
