# DESAIO: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

somapar = 0
matriz = [[], [], []]
for l in range(0, 3):
    for n in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{n}]: ')))
for lista in matriz:
    for elemento in lista:
        print(f'[{elemento:^6}]', end=' ')
        if elemento % 2 == 0:
            somapar += elemento
    print()
print(f'A soma dos valores pares é {somapar} ')
print(
    f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]} ')
print(f'O maior valor da segunda linha é {max(matriz[1])}. ')
