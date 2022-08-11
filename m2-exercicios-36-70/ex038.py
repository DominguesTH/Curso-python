# DESAFIO: Escreva um programa que leia dois numero inteiros e compare-os,  mostrando na tela uma mensagem: - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}.')
elif n1 == n2:
    print(f'Não existe valor maior, os número são iguais.')
else:
    print(f'{n2} é maior que {n1} ')
