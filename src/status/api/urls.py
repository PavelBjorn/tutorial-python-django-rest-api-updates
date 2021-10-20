from django.conf.urls import url

# TODO implement it
urlpatterns = [
    url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>.*))/$', StatusDetailAPIView.as_view()),
    url(r'^(?P<id>.*)/update/$', StattusUpdateAPIView.as_view()),
    url(r'^(?P<id>.*)/delete/$', StattusDeleteAPIView.as_view())
]
