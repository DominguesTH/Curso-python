# DESAIO: Crie um programa que faça o computador jogar Jokenpô com você.

# ===Módulos
from random import randint
from emoji import emojize
from time import sleep
# === Variáveis
itens = ('Pedra', 'Papel', 'Tesoura')
pedra = emojize(":oncoming_fist:")
papel = emojize(":hand_with_fingers_splayed:")
tesoura = emojize(":victory_hand:")
jokenpo1 = emojize(":raised_fist:")
jokenpo2 = emojize(":right-facing_fist:")
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA 
[1] PAPEL 
[2] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
if jogador > 2:
    print('!ERRO! Escolha o número de uma jogada válida e tente novamente.')
    quit()
print('-'*5, "COMPUTADOR", '-'*5)
sleep(1)
print(emojize(f' JO {jokenpo1}'))
sleep(1)
print(emojize(f" KEN {jokenpo2}"))
sleep(1)
if computador == 0:
    print(emojize(f" PÔ {pedra}", ))
    print(f'O computador escolheu: {pedra}')
    sleep(1)
    print('-=-'*10)
elif computador == 1:
    print(emojize(f" PÔ {papel}", ))
    sleep(1)
    print('-=-'*10)
    print(f'O computador escolheu: {papel}')
elif computador == 2:
    print(emojize(f" PÔ {tesoura}", ))
    sleep(1)
    print('-=-'*10)
    print(f'O computador escolheu: {tesoura}')
print('-'*30)
if jogador == 0:
    print(emojize(f"Você escolheu PEDRA: {pedra}", ))
elif jogador == 1:
    print(emojize(f"Você escolheu PAPEL: {papel}", ))
elif jogador == 2:
    print(emojize(f"Você escolheu TESOURA: {tesoura}", ))
print('-=-'*10)
if computador == 0:  # computador jogou "pedra"
    if jogador == 0:
        print('-'*5, "EMPATE", '-'*5)
    elif jogador == 1:
        print('-'*5, "VOCÊ VENCEU", '-'*5)
    elif jogador == 2:
        print('-'*5, "COMPUTADOR VENCEU", '-'*5)
elif computador == 1:  # computador jogou "Papel"
    if jogador == 0:
        print('-'*5, "COMPUTADOR VENCEU", '-'*5)
    elif jogador == 1:
        print('-'*5, "EMPATE", '-'*5)
    elif jogador == 2:
        print('-'*5, "VOCÊ VENCEU!", '-'*5)
elif computador == 2:  # computador jogou "Tesoura"
    if jogador == 0:
        print('-'*5, "VOCÊ VENCEU!", '-'*5)
    elif jogador == 1:
        print('-'*5, "VOCÊ PERDEU!", '-'*5)
    elif jogador == 2:
        print('-'*5, "EMPATE", '-'*5)

print('-=-'*10)

# print(emojize(":oncoming_fist:"))  # pedra
# print(emojize(":hand_with_fingers_splayed:"))  # papel
# print(emojize(":victory_hand:"))  # tesoura
# print(emojize(":raised_fist:"))  # jokenpo1
# print(emojize(":right-facing_fist:"))  # jokenpo2
