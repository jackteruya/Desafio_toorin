from core.models import Livros
from rest_framework import  serializers

class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros
        exclude = []