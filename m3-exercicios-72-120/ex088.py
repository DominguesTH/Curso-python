# DESAFIO: Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quanto jogos serão gerados e vai sortear 6 númerios entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# # ===== MEU CÓDIGO
# from time import sleep
# from random import randint
# print('-'*30)
# print('JOGA NA MEGA SENA')
# print('-'*30)
# palpites = []
# jogos = list()
# qnt = int(input('Quantos jogos você quer que eu sorteie? '))
# print(f'SORTEANDO OS {qnt} JOGOS')
# for p in range(1, (qnt+1)):
#     for n in range(1, 7):
#         numeros = (randint(1, 60))
#         if numeros not in palpites:
#             palpites.append(numeros)
#     sleep(1)
#     print(f'Jogo {p:^2}: {sorted(palpites)}')
#     jogos.append(palpites[:])
#     palpites.clear()
# # print(f'Os números sorteados foram {jogos}')
# print(f'BOA SORTE ')

# ==== CÓDIGO CORRIGIDO ====
from time import sleep
from random import randint
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)
palpites = list()
jogos = list()
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print('-='*3, f'SORTEANDO OS {qnt} JOGOS', '=-'*3)
sleep(1)
tot = 1
while tot <= qnt:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in palpites:
            palpites.append(numeros)
            cont += 1
        if cont >= 6:
            break
    jogos.append(palpites[:])
    palpites.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(l)}')
    sleep(1)
print('---', f'BOA SORTE', '---')
