"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/auth/jwt/$', obtain_jwt_token),
    url(r'api/auth/jwt/refresh/$', refresh_jwt_token),
    url(r'^api/updates/', include('updates.api.urls')),  # api/updates/1/ --> detail
    url(r'^api/status/', include('status.api.urls'))
]
