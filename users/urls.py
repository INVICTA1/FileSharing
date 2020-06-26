from django.conf.urls import url, include
from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login
from . import views
from django.contrib.auth.password_validation import password_changed
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as views_user

app_name = 'fileSharing'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^password_changed', views.a_change_password, name='a_change_password'),
    url(r'^account/files', views.user_files, name='user_files'),
]
