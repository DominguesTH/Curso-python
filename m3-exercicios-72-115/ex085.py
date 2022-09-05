# DESAFIO: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
valores = [[], []]
for v in range(1, 8):
    temp = int(input(f'Digite o {v}º valor: '))
    if temp % 2 == 0:
        valores[0].append(temp)
    elif temp % 2 == 1:
        valores[1].append(temp)
valores[0].sort()
valores[1].sort()
print('-='*35)
print(f'O números pares digitados foram {(valores[0])}')
print(f'Os números impares digitados foram {valores[1]}')
