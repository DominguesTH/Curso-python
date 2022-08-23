# DESAFIO: Crie um programa que crie uma matriz de dimensão 3*3 e preencha com valores lidos pelo teclado.  No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{n}]: ')))
for lista in matriz:
    for elemento in lista:
        print(f'[{elemento:^6}]', end=' ')
    print()


# # ==== CÓDIGO DO MESTRE ===
# matriz = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-='*30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l] [c]:^5}]', end='')
#     print()
