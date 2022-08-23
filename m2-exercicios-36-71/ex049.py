# DESAFIO: REFAÇA o DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

num = int(input('Digite o número para saber a tabuada: '))
print('-' * 11)
print(f'Tabuada do: {num}')
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
print('-' * 11)
