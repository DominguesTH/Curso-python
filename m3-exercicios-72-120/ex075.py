# DESAFIO: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.  C)Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'O primeiro número 3 foi digitado na {num.index(3) + 1}ª posição')
else:
    print('Não foi digitado nenhum número 3 ')
print('Os números pares inseridos foram: ', end='')
for n in num:
    if n % 2 == 0:
        par = n
        print(f'{par} - ', end=' ')
