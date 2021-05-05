"""
Função que receba um dict de dados, e retorne uma versão com os nomes dos
atributos no formato 'camelCase'.

>>> print(snake_to_camel({"some_name_last_na": "lorem ipsum"}))
{'someNameLastNa': 'lorem ipsum'}
>>> print(snake_to_camel({"some_name": "lorem ipsum"}))
{'someName': 'lorem ipsum'}
"""

def snake_to_camel(dados:dict):
    for key, value in dados.items():
        if '_' in key:
            newKey = list(key.split('_'))
            camel = newKey[0] + ''.join(x.title() for x in newKey[1:])
        return {camel: value}


if __name__ == '__main__':
    print(snake_to_camel({"some_name_last_na":"lorem ipsum"}))