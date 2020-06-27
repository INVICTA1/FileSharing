import socket

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Document(models.Model):
    name = models.CharField(max_length=100)
    path = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    url = models.CharField(max_length=100, default=str(socket.gethostbyname(socket.gethostname())))
    expires_doc = models.DateTimeField(default=timezone.now() + timedelta(days=1))

