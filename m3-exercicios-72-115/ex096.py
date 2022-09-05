# DESAFIO: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
numeros = list()


def area(l, c):
    res = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {res}m². ')


print('Controle de terrenos')
print('-' * 20)
numeros.append(float(input('LARGURA (m): ')))
numeros.append(float(input('COMPRIMENTO (m): ')))
area(numeros[0], numeros[1])
