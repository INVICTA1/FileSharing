from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from django.db import models
from .user import UserSerializer


class File(models.Model):
    pass
    # id = models.ForeignKey(UserSerializer, on_delete=models.CASCADE)
    # name = models.CharField(null=False)
    # date_added = models.DateTimeField(auto_now_add=True)


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'id_user')


class FileViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a file instance.

    list:
        Return all files, ordered by most recently joined.

    create:
        Create a new file.

    delete:
        Remove an existing file.

    partial_update:
        Update one or more fields on an existing file.

    update:
        Update a file.
    """
    queryset = ["1", "2", "3"]
    serializer_class = FileSerializer
