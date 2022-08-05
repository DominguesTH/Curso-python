# DESAFIO: Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

# =========Meu código================
from calendar import c


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f' O menor valor digitado foi: {menor}')
print(f' O maior valor digitado foi: {maior}')
