from django.conf.urls import url

from .views import StatusAPIView
from .views import StatusCreateAPIView
from .views import StatusDetailAPIView
from .views import StatusUpdateAPIView
from .views import StatusDeleteAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', StatusUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', StatusDeleteAPIView.as_view())
]
