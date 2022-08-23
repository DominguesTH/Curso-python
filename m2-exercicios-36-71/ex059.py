# DESAFIO: Crie um programa que leia dois valores e mostre um menu na tela: [1]somar [2]multiplicar [3]maior [4]novos números [5]sair do programa.   Seu programa deverá realizar a operação solicidade em cada caso.


from time import sleep
opção = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while opção != 5:
    opção = int(input('''----- Suas opções são -----'
  [1] - Somar
  [2] - Multiplicar
  [3] - Maior
  [4] - Novos números
  [5] - Sair do programa
-> O que deseja fazer?: '''))
    if opção == 1:
        res = n1 + n2
        print(f'A soma entre {n1} + {n2} é {res}')
    elif opção == 2:
        res = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é: {res}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'{n1} é menor que {n2}')
        elif n1 == n2:
            print(f'Os valores são iguais.')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Saindo...')
    else:
        print('=-=-=-=-=- Está opção não é valida, tente novamente. -=-=-=-=-=')
    sleep(2)
print('-'*5, 'FIM', '-'*5)
