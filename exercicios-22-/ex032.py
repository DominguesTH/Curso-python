# DESAFIO: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# =========Meu código================
from calendar import isleap
ano = int(input('Digite um ano: '))
if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')
