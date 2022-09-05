# DESAFIO: Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep
jogador = dict()
time = list()
while True:
    gols = []
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! digite apenas S ou N. ')
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    if continuar == 'N':
        break
print('-=' * 40)
print(f'{"cod":^5}{"Nome":^10}{"Gols":^20}{"Total":^20}')
print('-' * 50)
for i, k in enumerate(time):
    print(f'{i!s:^5}{k["nome"]!s:^10}{k["gols"]!s:^20}{k["total"]!s:^20}')
print('-=' * 40)
opcao = ' '
while opcao != 999:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    elif opcao > len(time) - 1:
        print('-' * 50)
        print(
            f'ERRO! Náo existe jogador com o código {opcao}! Digite um código válido. ')
        print('-' * 50)
    else:
        print('-' * 50)
        print(f'-- LEVANTAMENTO DO JOGADOR {time[opcao]["nome"]}: ')
        print('-' * 50)
        for k, v in enumerate(time[opcao]['gols']):
            print(f'  => Na partida {k + 1}, fez {v} gols. ')
        print()
        print(f'>> Foi um total de {sum(time[opcao]["gols"])} gols. <<')
        print()
sleep(1)
print()
print('ENCERRANDO - VOLTE SEMPRE :) ')
sleep(1)
print()
print('FIM')
print()
