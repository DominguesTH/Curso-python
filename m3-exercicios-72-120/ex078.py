# DESAFIO: Faça um programa que leia 5 valores numéricos e guar-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


maior = menor = 0
numeros = [int(input('Digite um valor para a posição 0: ')),
           int(input('Digite um valor para a posição 1: ')),
           int(input('Digite um valor para a posição 2: ')),
           int(input('Digite um valor para a posição 3: ')),
           int(input('Digite um valor para a posição 4: '))]
for p, v in enumerate(numeros):
    if p == 0:
        maior = menor = v
        pmaior = p
    else:
        if v <= menor:
            menor = v
            pmenor = p
        if v >= maior:
            maior = v
            pmaior = p
    print(f'posição {p} , número: {v}. O maior: {maior}. O menor {menor} ')
print('=-'*30)
print(f'Você digitou os números {numeros}')
print(
    f'O maior número digitado foi {max(numeros)} nas posições ', end='')
for i, va in enumerate(numeros):
    if va == maior:
        print(f'{i}...', end='')
print(
    f'\nO menor número digitado foi {min(numeros)} nas posições ', end='')
for i, va in enumerate(numeros):
    if va == menor:
        print(f'{i}...', end='')


# #===== CÓDIGO DO MESTRE ===
listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()

# ==== Outras maneiras

numeros = []
pmaior = pmenor = 1
for b1 in range(1, 6):
    numeros.append(int(input(f'Digite o {b1}¹ valor: ')))
pmaior += numeros.index(max(numeros))
pmenor += numeros.index(min(numeros))
print(numeros)
print(f'O maior é \33[35m{max(numeros)}\33[m', end=' ')
print(f'na posição \33[35m{pmaior}\33[m')
print(f'O menor é \33[35m{min(numeros)}\33[m', end=' ')
print(f'na posição \33[35m{pmenor}\33[m')


# === OUTRA MANEIRA ========

valores = list()  # Lista vazia.

# Armazena 5 valores digitados na lista.
for c in range(5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

# Mostra os valores digitados.
print(f'\nVocê digitou os valores {valores}')

# Verifica a quantidade de maiores valores digitados, se for apenas 1
# mostra no singular, se for mais mostra no plural.
if valores.count(max(valores)) == 1:
    print(
        F'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}.')
else:
    print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
    for c, v in enumerate(valores):
        if v == max(valores):
            print(c, end='... ')
    print()

# Verifica a quantidade de menores valores digitados, se for apenas 1
# mostra no singular, se for mais mostra no plural.
if valores.count(min(valores)) == 1:
    print(
        f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}.')
else:
    print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
    for c, v in enumerate(valores):
        if v == min(valores):
            print(c, end='... ')
