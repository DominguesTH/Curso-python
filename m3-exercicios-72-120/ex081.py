# DESAFIO: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.  C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
dig = 1
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'S':
        dig += 1
    if continuar in 'N':
        break
num = numeros[:]
numeros.sort(reverse=True)
print('-=-'*50)
print(f'Você digitou {dig} elemnetos.')
print(
    f'Os valores em ordem decrescente são {numeros}')
if 5 in num:
    print('O valor 5 aparece nas posições: ', end='')
    for p, n in enumerate(num):
        if n == 5:
            print(p, end='...')
    print(f' Posição digitada: {num}')
else:
    print('Não encontrei nenhum número 5 na lista...')

# # ===== CÓDIGO DO MESTRE ======

# valores = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-='*30)
# print(f'Você digitou {len(valores)} elementos.')
# valores.sort(reverse=True)
# print(f'Os valores na ordem decrecente são {valores}')
# if 5 in valores:
#     print('O valor 5 faz parte da lista')
# else:
#     print('O valor 5 não foi encontrado na lista!')
