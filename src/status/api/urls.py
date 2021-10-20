from django.conf.urls import url

from .views import StatusAPIView
from .views import StatusCreateAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>.*))/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StattusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StattusDeleteAPIView.as_view())
]
