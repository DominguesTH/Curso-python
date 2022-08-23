# DESAFIO: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:  -1 para binário  -2 para octal -3 para hexadecimal
n = int(input('Digite um número: '))
e = int(input('Digite o número que corresponde a opção que deseja converter:\n'
              '1 - Binário\n'
              '2 - Octal\n'
              '3 - Hexadecimal\n'))
if e == 1:
    print(f'Convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif e == 2:
    print(f'Convertido para OCTAL é igual a {oct(n)[2:]}')
elif e == 3:
    print(f'Convertido para BINÁRIO é igual a {hex(n)[2:]}')
else:
    print('Escolha uma opção válida.')
