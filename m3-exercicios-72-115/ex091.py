# DESAFIO: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogadoo1': randint(1, 6),
             'jogadoo2': randint(1, 6),
             'jogadoo3': randint(1, 6),
             'jogadoo4': randint(1, 6)}
ranking = list()
print(f'Valores sorteados:')
for k, v in jogadores.items():
    sleep(.8)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*40)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i}º lugar: {v[0]} com {v[1]}')
