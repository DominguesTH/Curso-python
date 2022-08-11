# DESAFIO: Desenvolva um programa que leia seis números inteiros e mostre asoma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
print('-'*5,  'SOMANDO APENAS NÚMEROS PARES', '-'*5)
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        s = s + n
        cont += 1
print(
    f'Vcoê inseriu {cont} números PARES e a soma deles é: {s}')
