from django import forms
from django.db import models
from rest_framework_dyn_serializer import serializers
from rest_framework import viewsets


class Dog():
    class Document(models.Model):
        description = models.CharField(max_length=255, blank=True)
        document = models.FileField(upload_to='documents/')
        uploaded_at = models.DateTimeField(auto_now_add=True)


class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'age')


class DogViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given dog.

    list:
        Return a list of all dogs.

    create:
        Create a new dog.

    destroy:
        Delete a dog.

    update:
        Update a dog.

    partial_update:
        Update a dog.
    """

    serializer_class = DogSerializer
