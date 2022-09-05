# DESAFIO: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado de show, que será um valor logico (opcinal)indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from math import factorial


def fatorial(n, show=False):
    """-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return (f'O valor de {n}! é = {fat}')


# -----
print(fatorial(int(input("Digite o valor de n: ")), show=False))
print('-'*40)
help(fatorial)
