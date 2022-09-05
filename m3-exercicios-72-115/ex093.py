# DESAFIO: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final.  tudo isso será guardado em um dicionario, incluindo o  total de gols feitos durante o campeonato.

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 40)
print(f'{jogador}')
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'  => Na partida {k + 1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
print()
