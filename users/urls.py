from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
app_name = 'fileSharing'
urlpatterns = [
    # url(r'^login/$', LoginView, {'template_name': 'users/login.html'},name='login'),
    url(r'^/$',views.get_file,name='get_file'),
    url(r'^(?P<file_id>\d+)',views.get_file,name='get_file'),

]
