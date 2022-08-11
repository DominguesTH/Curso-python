# DESAFIO: Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.

from time import sleep
print('='*10, "MOSTRNADO APENAS OS MULTIPLOS DE 3", '='*10)
n1 = int(input('De: '))
n2 = int(input('Até:  ')) + 1
s = 0
cont = 1
for c in range(n1, n2):
    if c % 3 == 0:
        if c % 2 == 1:
            cont = cont + 1
            s += c
sleep(1)
print(
    '-'*10, f" A soma de todos os {cont} valores solicitados é de {s} ", '-'*10)
