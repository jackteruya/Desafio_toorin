'''from rest_framework import viewsets
from booksRestApi.api import serializers
from booksRestApi.core import models

class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializers
    queryset = models.Livros.objects.all()'''

'''class LivrosApiView(APIView):
    def get(self, request):
        livros = Livros.objects.all()
        output = [{'titulo': livro.titulo,
                   'isbn': livro.isbn,
                   'autor': livro.autor,
                   'editora': livro.editora,
                   'numero paginas': livro.numeros_paginas,
                   'descricao': livro.descricao
                   } for livro in livros]
        return Response(output)

    def post(self, request):
        livro = Livros.objects.create(titulo=request.data.get('titulo'),
                                      isbn=request.data.get('isbn'),
                                      autor=request.data.get('autor'),
                                      editora=request.data.get('editora'),
                                      numeros_paginas=request.data.get('numero paginas'),
                                      descricao=request.data.get('descricao')
                                      )
        output = {
                'titulo': livro.titulo,
                'isbn': livro.isbn,
                'autor': livro.autor,
                'editora': livro.editora,
                'numero paginas': livro.numeros_paginas,
                'descricao': livro.descricao
            }
        return Response(output)

livros_view = LivrosApiView.as_view()'''

'''@api_view()
def livros_view(request):
    livros = Livros.objects.all()
    output = [{'titulo': livro.titulo,
               'isbn': livro.isbn,
               'auto': livro.isbn,
               'editora': livro.editora,
               'numero paginas': livro.numeros_paginas,
               'descricao': livro.descricao

    } for livro in livros]

    return Response(output)
'''