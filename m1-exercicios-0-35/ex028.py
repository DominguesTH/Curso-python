# DESAFIO: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.  O programa deverá escrever na tela se o usuário venceu ou perdeu.

# =========Meu código================
from random import randint
from time import sleep
print('=' * 55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=' * 55)
nsorteio = randint(0, 5)
n = int(input('Qual número estou pensando?: '))
print('-=-' * 18)
print('Hum.... Só queria dizer que....')
print('-=-' * 18)

sleep(1.5)
if n == nsorteio:
    print('-' * 50)
    print('Acertou misseravii! ')
    print('-' * 50)
else:
    print('-' * 50)
    print(f'Você errrouu haha pensei no número {nsorteio}')
    print('-' * 50)
print('--FIM DE JOGO--')
