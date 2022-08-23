# DESAFIO: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# #======= MEU CÓDIGO ========
# numExt = 'Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
# num = int(input('Digite um número entre 0 e 20: '))
# while num < 0 or num > 20:
#     num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
# print(f'Você digitou o número: {numExt[num]}')

# ======= CÓDIGO DO MESTRE ========

# from time import sleep

# cont = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
#         'Doze', 'treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {cont[num]}')
# sleep(1)
# print(f'FINALIZANDO ... Volte sempre!')
# sleep(1.5)
# print('FIM')

# ============ APRIMORANDO ========  -> Incluindo a opção de continuar a diigitiar novos números.
from time import sleep
cont = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
        'Doze', 'treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    continuar = ' '
    if num < 0 or num > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {cont[num]}')
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'N':
            break
sleep(0.5)
print(f'FINALIZANDO ... Volte sempre!')
sleep(1)
print('FIM')
