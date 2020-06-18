from django.conf.urls import url
from . import views

app_name = 'fileSharing'
urlpatterns = [
    url(r'', views.simple_upload, name='upload_file'),
    url(r'login',views.user_files,name='user_files')
]
