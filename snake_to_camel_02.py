"""
Função que receba um dict de dados, e retorne uma versão com os nomes dos
atributos no formato 'camelCase'.

>>> print(snake_to_camel({"some_name_last_na": "lorem ipsum"}))
{'someNameLastNa': 'lorem ipsum'}
>>> print(snake_to_camel({"some_name": "lorem ipsum"}))
{'someName': 'lorem ipsum'}
"""


def snake_to_camel(data: dict):
    newData = {}
    for key, value in data.items():
        if '_' in key:
            new_key = list(key.split('_'))
            camel = new_key[0] + ''.join(x.title() for x in new_key[1:])
            newData[camel] = value
        else:
            newData[key] = value
    return newData


if __name__ == '__main__':
    print(snake_to_camel({"some_name_last_na": "lorem ipsum", 'nome':'Jose', 'idade_now':28}))
