# DESAFIO: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# =========Meu código================
from datetime import date
from calendar import isleap
ano = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
