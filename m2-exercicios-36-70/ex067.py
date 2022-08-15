# DESAFIO: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor figitado pelo usuário. O programa será interrompido quando o número solicidado for negativo.


from time import sleep
while True:
    num = int(input('Digite o número para saber a tabuada: '))
    if num < 0:
        break
    print('-' * 11)
    print(f'Tabuada do: {num}')
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    print('-' * 11)
sleep(1.5)
print('PROGRAMA ENCERRADO. Volte sempre!')
