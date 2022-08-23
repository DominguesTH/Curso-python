# DESAFIO: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).upper().strip().replace(" ", "")
if frase == frase[::-1]:
    print('Palíndromo')
else:
    print('Não é um Palíndromo')
