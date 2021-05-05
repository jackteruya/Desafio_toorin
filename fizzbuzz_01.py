"""
Função tem com objetivo retornar uma lista de 1 a 100 com as seguintes regras:
    1 - Caso o número seja múltiplo de 3, substituir por "Fizz!"
    2 - Caso o número seja múltiplo de 5, substituir por "Buzz!"
    3 - Caso o número seja múltiplo de 3 e 5, substituir por "FizzBuzz!"

    >>> fizz_buzz()
    [1, 2, 'Fizz!', 4, 'Buzz!', 'Fizz!', 7, 8, 'Fizz!', 'Buzz!', 11, 'Fizz!',
    13, 14, 'FizzBuzz!', 16, 17, 'Fizz!', 19, 'Buzz!', 'Fizz!', 22, 23,
    'Fizz!', 'Buzz!', 26, 'Fizz!', 28, 29, 'FizzBuzz!', 31, 32, 'Fizz!', 34,
    'Buzz!', 'Fizz!', 37, 38, 'Fizz!', 'Buzz!', 41, 'Fizz!', 43, 44,
    'FizzBuzz!', 46, 47, 'Fizz!', 49, 'Buzz!', 'Fizz!', 52, 53, 'Fizz!',
    'Buzz!', 56, 'Fizz!', 58, 59, 'FizzBuzz!', 61, 62, 'Fizz!', 64, 'Buzz!',
    'Fizz!', 67, 68, 'Fizz!', 'Buzz!', 71, 'Fizz!', 73, 74, 'FizzBuzz!', 76,
     77, 'Fizz!', 79, 'Buzz!', 'Fizz!', 82, 83, 'Fizz!', 'Buzz!', 86, 'Fizz!',
     88, 89, 'FizzBuzz!', 91, 92, 'Fizz!', 94, 'Buzz!', 'Fizz!', 97, 98,
     'Fizz!', 'Buzz!']
"""


def fizz_buzz():
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


if __name__ == '__main__':
    print(fizz_buzz())
