# DESAFIO: Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (considerar maioridade de : 25anos)

from datetime import date
s = 0
tmaior = 0
tmenor = 0
atual = date.today().year
for c in range(1, 7):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu?  '))
    idade = atual - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print(f' {tmaior} pessoas são maiores de idade \n {tmenor} são menores de idade.')
