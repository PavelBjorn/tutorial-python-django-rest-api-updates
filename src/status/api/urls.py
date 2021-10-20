from django.conf.urls import url

from .views import StatusAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
]
