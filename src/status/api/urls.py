from django.conf.urls import url

from .views import StatusAPIView
from .views import StatusDetailAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view()),
]
