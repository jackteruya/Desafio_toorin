from rest_framework import viewsets
from book.api import serializers
from core import models

class LivrosViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializers
    queryset =  models.Livros.objects.all()
