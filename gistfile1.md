## Teste de conhecimentos gerais Python - v2.0

Você pode usar qualquer biblioteca que julgar necessária para resolver as questões abaixo,
apenas deixe documentado em um arquivo requirements.txt para podermos instalar posteriormente.
Ao finalizar o teste, salve este arquivo e o arquivo requirements.txt em um zip e envie pra gente!

1. FizzBuzz!
    Construa uma função que retorne uma lista, contando
    de 1 a 100, enquanto segue as seguintes regras:
    - Caso o número seja múltiplo de 3, substituir por "Fizz!"
    - Caso o número seja múltiplo de 5, substituir por "Buzz!"
    - Caso o número seja múltiplo de 3 e 5, substituir por "FizzBuzz!"

2. snake_case -> camelCase
    Construa uma função que receba um dict de dados, e retorne uma versão
    com os nomes dos atributos no formato 'camelCase', ao invés de 'snake_case'.
    Exemplo:
    data = {
        "some_name": "lorem ipsum"
    }
    new_data = {
        "someName": "lorem ipsum"
    }

3. OMDb API Use Case
    Construa uma função que faça uma request à API de filmes e seriados OMDb API (http://www.omdbapi.com).
    Sua função deverá receber o título do filme a ser pesquisado, e retornar o status e o body da response.
    Usaremos a nossa API Key para realizar os testes, não é necessário manter a sua no código quando 
    for enviá-lo de volta :)

4. Books Rest API
    Construa uma API Rest simples em Django, usando Django Rest Framework ou Django Ninja, e um
    banco de dados Sqlite.
    Sua API deve conter um CRUD de livros, e cada livro deve ter os seguintes dados cadastrados:
    - Título
    - ISBN
    - Autor(es)
    - Editora
    - Edição
    - Número de páginas
    - Descrição rápida
    Faça upload do projeto para o seu GitHub, e retorne o link dele na quarta função da classe
    abaixo. Ah, e não esqueça de deixar seu repositório público!

    Boa sorte!




```
from typing import Tuple


class Test:
    def fizz_buzz(self) -> list:
        list_fizz_buzz = []
        for x in range(1, 101):
            if x % 3 == 0 and x % 5 == 0:
                list_fizz_buzz.append("FizzBuzz!")
            elif x % 3 == 0:
                list_fizz_buzz.append("Fizz!")
            elif x % 5 == 0:
                list_fizz_buzz.append("Buzz!")
            else:
                list_fizz_buzz.append(x)
        return list_fizz_buzz

    def snake_to_camel(self, data: dict) -> dict:
        new_data = {}
        for key, value in data.items():
            if '_' in key:
                new_key = list(key.split('_'))
                camel = new_key[0] + ''.join(x.title() for x in new_key[1:])
                new_data[camel] = value
            else:
                new_data[key] = value
        return new_data

    def get_omdb_movie(self, title: str) -> Tuple[int, dict]:
        response = requests.get(f'http://www.omdbapi.com/?apikey=fb69039d&t={title}') #import requests
        data = (response.status_code, response.json())
        return data

    def get_awesome_project_link(self) -> str:
        return "https://github.com/jackteruya/Desafio_toorin.git" 

    def run(self):
        snake_data = {
            "first_name": "Jackson",
            "last_name": "Souza",
            "e-mail": "email@email.com",
            "cpf": "156.999.777-11",
            "marital_status": "Solteiro",
            "age": 35,
            "mobile_phone": "1111111111",
        }
        movie_name = "Toy Story"

        print("1. FizzBuzz!")
        fizzbuzz_list = self.fizz_buzz()
        print(fizzbuzz_list)

        print("2. snake_case -> camelCase")
        camel_data = self.snake_to_camel(snake_data)
        print(camel_data)

        print("3. OMDb API Use Case")
        status, resp = self.get_omdb_movie(movie_name)
        print("Status: %d\nBody: %s" % (status, resp))

        print("4. Books Rest API")
        awesome_api_link = self.get_awesome_project_link()
        print(awesome_api_link)



test_case = Test()
test_case.run()
```