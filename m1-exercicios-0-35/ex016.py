# DESAFIO: Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.  Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

# =====Com import=======
from math import trunc
num = float(input('Digite um número: '))
print(f'A porção inteira de {num} é igual a {trunc(num)} ')

# =====Sem import=======
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')
