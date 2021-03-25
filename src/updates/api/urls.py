from django.conf.urls import url

from .views import (
    UpdateModelListAPI
)

urlpatterns = [
    url(r'^$', UpdateModelListAPI.as_view()),
]
