# DESAFIO: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pesssoas mais pesadas. C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
todos_pesos = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
for peso in pessoas:
    todos_pesos.append(peso[1])
maior = max(todos_pesos)
menor = min(todos_pesos)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg, das seguintes pessoas: ', end='')
for pess in pessoas:
    if pess[1] == maior:
        print(f'{pess[0]}', end='...')
print(f'\nO menor peso foi de {menor}Kg, das seguintes pessoas: ', end='')
for pess in pessoas:
    if pess[1] == menor:
        print(f'{pess[0]}', end='... ')
