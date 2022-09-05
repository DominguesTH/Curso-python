# DESAFIO: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenbas os valores pares e os valores impares digitados respectivamente. Ao final, mostre o conteúdo das três listas geras

numeros = list()
npar = list()
ninpar = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).upper().strip()
    if continuar in 'N':
        break
for n in numeros:
    if n % 2 == 0 and n != 0:
        npar.append(n)
    elif n % 2 == 1:
        ninpar.append(n)
print('-='*30)
print(f'A lista completa é {numeros}')
if len(npar) == 0:
    print('Não tem números pares na lista.')
else:
    print(f'A lista de pares é {npar}')
if len(ninpar) == 0:
    print('Não tem números ímpares na lista')
else:
    print(f'A lista de ímpares é {ninpar}')
