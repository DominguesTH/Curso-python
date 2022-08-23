# --> Mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista.
names = ["Sam", "Peter", "James", "Julian", "Ann"]
print(*names, sep=", ")

num = [1, 5, 9, 1, 6, 8]
# --- * remove os colchetes
print(*num)
num[1] = 2
# --Adiciona um elemento  na lista
num.append(7)
print(*num)
# ---  inseriu o número 0 na posição 2 da lista
num.insert(2, 0)
# --- Remove o ultimo elemento da lista se não tiver nenhum parametro
num.pop()
# --- Coloca os números em ordem
num.sort()
print(*num)
# --- Coloca os números em ordem reversa
num.sort(reverse=True)
print(*num)
# ---  Mostra quantos elementos tem na lista
print(f'Essa lista tem {len(num)} elementos')

# --- Verificando se existe o valor 4 na lista. caso tenha, ira removelo, senão ira dizer que não encontrou o numero 4
num = [1, 5, 9, 1, 6, 8]
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei nenhum número 4')
print(*num)

# == ENCONTRANDO VALORES DOS ELEMENTOS DA LISTA "INDICE"
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# == LENDO VALORES PELO TECLADO
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# -- Cria uma cópia da lista a para lista b
a = [2, 3, 6, 8]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
