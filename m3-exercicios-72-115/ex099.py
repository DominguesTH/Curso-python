# DESAFIO: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetro com valores inteiros.  Seu programa tem que anasalisar todos valores e dizer qual deles é o maior.


from time import sleep


def maior(*num):
    print('-='*40)
    print('Analisando os valores passados... ')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(.3)
    print(f'Foram informados {len(num)} valores ao todo. ')
    print(f'O maior número informado foi {max(num)}')
    # if len(p) == 0:
    #     print('-='*40)
    #     print('Analisando os valores passados... ')
    #     print(f'{p} Foram informados {len(p)} valores ao todo. ')
    #     print(f'O maior número informado foi {max(p)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(2, 5)
maior(6)
maior(0)


# from random import randint


# def maior(*p):
#     if len(p) == 6:
#         print('-='*40)
#         print('Analisando os valores passados... ')
#         print(f'{p} Foram informados {len(p)} valores ao todo. ')
#         print(f'O maior número informado foi {max(p)}')
#     if len(p) == 3:
#         print('-='*40)
#         print('Analisando os valores passados... ')
#         print(f'{p} Foram informados {len(p)} valores ao todo. ')
#         print(f'O maior número informado foi {max(p)}')
#     if len(p) == 2:
#         print('-='*40)
#         print('Analisando os valores passados... ')
#         print(f'{p} Foram informados {len(p)} valores ao todo. ')
#         print(f'O maior número informado foi {max(p)}')
#     if len(p) == 1:
#         print('-='*40)
#         print('Analisando os valores passados... ')
#         print(f'{p} Foram informados {len(p)} valores ao todo. ')
#         print(f'O maior número informado foi {max(p)}')
#     if len(p) == 0:
#         print('-='*40)
#         print('Analisando os valores passados... ')
#         print(f'{p} Foram informados {len(p)} valores ao todo. ')
#         print(f'O maior número informado foi {max(p)}')


# # numeros = [randint(0, 10), randint(0, 10), randint(
# #     0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(2, 5)
# maior(6)
# maior(0)
