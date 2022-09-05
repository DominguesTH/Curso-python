# DESAFIO: Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os vcalores únicos digitados, em ordem crescente.


num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor duplicado! Não vou adicionar..')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'Você digitou os números {sorted(num)}')
