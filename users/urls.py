from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

app_name = 'fileSharing'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
]
