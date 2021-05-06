from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=50)
    edicao = models.CharField(max_length=10)
    numeros_paginas = models.CharField(max_length=10)
    descricao = models.TextField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'livro'