from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'fileSharing'
urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^password_changed', views.a_change_password, name='a_change_password'),
    url(r'^account/files', views.user_files, name='user_files'),
    path(r'delete/<str:name>/', views.del_user_files, name='del_user_files'),

]
