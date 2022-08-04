# DESAFIO: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.  O programa deverá escrever na tela se o usuário venceu ou perdeu.

# =========Meu código================
import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
nsorteio = random.randint(0, 5)
n = int(input('Qual número estou pensando?: '))

if n == nsorteio:
    print('Acertou misseravii! ')
else:
    print(f'Errrouu haha pensei no número {nsorteio}')
print('--FIM DE JOGO--')
