from django.conf.urls import url, include
from rest_framework import routers
from .model.user import UserViewSet
from .model.file import FileViewSet

app_name = 'fileSharing'

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
# router.register(r'', FileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
