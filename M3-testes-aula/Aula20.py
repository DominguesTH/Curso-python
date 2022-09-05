# Criando uma função para somar
print('-'*30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# referenciando
soma(8, 2)
soma(a=2, b=8)
print('-'*30)


# contanto os números com laço 'for' dentro da tubla criada com a função.
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 3, 5, 10)
contador(2, 3, 5, 8, 15)
contador(2, 3, 5, 16, 2)

print('-'*30)

# Usando def de outra forma para junto com uma função


def contador(*num):
    tam = len(num)
    print(f' Recebi os valores {num} e  sáo ao todo {tam} números')


contador(2, 3, 5, 10)
contador(2, 3, 5, 8, 15)
contador(2, 3, 5, 16, 2)
print('-'*30)


def dobra(numeros):
    pos = 0
    while pos < len(numeros):
        numeros[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

print('-'*30)


def somar(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somar(5, 2)
somar(2, 9, 4)
print('-'*30)
