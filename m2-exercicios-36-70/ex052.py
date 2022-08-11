# DESAFIO: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from colorama import Fore,  Back,  Style
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(Fore . GREEN, end=' ')
        tot += 1
    else:
        print(Fore . RED, end=' ')
    print(c, Style.RESET_ALL, '→', end='')
print(Fore . YELLOW, f' \n O número {num} foi divisível {tot} vezes ',
      end='' + Style.RESET_ALL)
if tot == 2:
    print(Fore . GREEN,
          f'E por isso ele é um número primo', Style.RESET_ALL)
else:
    print(
        Fore . RED, f'E por isso não é um número primo', Style.RESET_ALL)
