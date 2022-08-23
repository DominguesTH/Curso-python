# DESAFIO: Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


# from random import randint
# xvencida = 0
# print('-=-'*10)
# print('VAMOS JOGAR PAR OU ÍMPAR')
# print('-=-'*10)
# while True:
#     computador = randint(0, 10)
#     njogador = int(input('Digite um valor: '))
#     jogador = str(input('Par ou Ímpar?: [P/I] ')).upper().strip()[0]
#     soma = njogador + computador
#     if soma % 2 == 0 and jogador == 'P':
#         print('--'*20)
#         print(
#             f'Você jogou {njogador} e o computador {computador}. Total de {soma} DEU PAR! ')
#         xvencida += 1
#         print('--'*20)
#     elif soma % 2 == 1 and jogador == 'I':
#         print('--'*20)
#         print(
#             f'Você jogou {njogador} e o computador {computador}. Total de {soma} DEU IMPAR! ')
#         print('--'*20)
#         xvencida += 1
#     elif soma % 2 == 1 and jogador == 'P':
#         print('--'*20)
#         print(
#             f'Você jogou {njogador} e o computador {computador}. Total de {soma} DEU IMPAR! ')
#         print('=-'*20)
#         break
#     elif soma % 2 == 0 and jogador == 'I':
#         print('--'*20)
#         print(
#             f'Você jogou {njogador} e o computador {computador}. Total de {soma} DEU PAR! ')
#         print('=-'*20)
#         break
#     elif jogador not in 'IP':
#         print('TENTE NOVAMENTE')
# print('Você PERDEU!')
# print('=-'*20)
# print(f'GAME OVER! você venceu {xvencida} vezes')

# ======= CÓDIGO DO MESTRE =======

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(
        f'Você jogou {jogador} e o computador {computador}. Total de {total}. ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
