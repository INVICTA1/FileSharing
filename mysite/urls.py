from django.conf.urls import url

from fileSharing import settings
from . import views
from django.conf.urls.static import static

app_name = 'fileSharing'
urlpatterns = [
    url(r'', views.simple_upload, name='upload_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
