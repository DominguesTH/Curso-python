# DESAFIO: Melhore o jogo desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quanto palpites foram necessários para vencer.

# ====== MEU CÓDIGO ======
# from random import randint
# from time import sleep
# print('=' * 55)
# print('Vou pensar em um número entre 0 e 10.')
# print('=' * 55)
# sleep(1.5)
# print('-- Tente adivinhar..... ')
# nsorteio = randint(0, 5)
# n = 999
# tentativas = 1
# while nsorteio != n:
#     n = int(input('Qual número estou pensando?: '))
#     sleep(1)
#     if n == nsorteio:
#         print('-' * 50)
#         print('Acertou misseravii! ')
#         print('-' * 50)
#     if n > nsorteio:
#         tentativas += 1
#         print('-' * 50)
#         print(f'Menos.... tente novamente!')
#         print('-' * 50)
#     if n < nsorteio:
#         tentativas += 1
#         print('-' * 50)
#         print(f'Mais.... tente novamente!')
#         print('-' * 50)

# print(f'Você precisou de {tentativas} tentativas para vencer!')
# sleep(1.5)
# print('=' * 55)
# print('--FIM DE JOGO--')
# print('=' * 55)

# ======CÓDIGO DO MESTRE ======
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... tente mais uma vez.')
        elif jogador > computador:
            print('Menos.... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
