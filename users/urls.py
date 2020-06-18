from django.conf.urls import url
from django.contrib.auth import login,logout
from django.contrib.auth.views import logout_then_login
from . import views

app_name = 'fileSharing'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.dashboard, name='dashboard'),
]
