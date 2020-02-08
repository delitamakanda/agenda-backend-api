from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views


urlpatterns = [
    url(r'^login/$', views.AuthAPIView.as_view(), name='auth_login'),
    url(r'^register/$', views.RegisterAPIView.as_view(), name='auth_register'),
    url(r'^jwt/$', obtain_jwt_token, name='jwt'),
    url(r'^refresh/$', refresh_jwt_token, name='refresh'),
    url(r'^(?P<username>\w+)/$', views.UserDetailAPIView.as_view(), name='detail'),
]
