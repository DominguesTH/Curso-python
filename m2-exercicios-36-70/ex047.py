# DESAFIO: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('='*10, "MOSTRNADO APENAS O NÚMEROS PARES", '='*10)
n1 = int(input('De: '))
n2 = int(input('Até:  ')) + 1
for c in range(n1, n2):
    if c % 2 == 0:
        print(f'{c}')
