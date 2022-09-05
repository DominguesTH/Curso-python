# DESAFIO: Faça um programa que tenha uma lista chamada número e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
# from random import randint

# numeros = list()
# somavalor = []

# print('-='*30)


# def sorteio(s):
#     s = [randint(0, 10), randint(0, 10), randint(
#         0, 10), randint(0, 10), randint(0, 10)]
#     numeros.append(s)
#     print(f'Sorteando 5 valores da lista: {s} pronto!')


# def somapar(som):
#     for v in som[0]:
#         if v % 2 == 0:
#             somavalor.append(v)
#     print(f'Somando os valores pares de {som}, temos {sum(somavalor)}')


# sorteio(0)
# somapar(numeros)
# print()


# OUTRA MANEIRA
from random import randint


print('-='*30)


def sorteio(lista):
    print(f'Somando os 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    print(f'PRONTO!')


def somapar(som):
    somavalor = []
    for v in som:
        if v % 2 == 0:
            somavalor.append(v)
    print(f'Somando os valores pares de {som}, temos {sum(somavalor)}')


numeros = list()
sorteio(numeros)
somapar(numeros)
