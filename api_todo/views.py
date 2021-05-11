from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models


class TodoViewSet(ModelViewSet):
    serializer_class = serializers.TodoSerializer   
    queryset = models.Todo.objects.all()