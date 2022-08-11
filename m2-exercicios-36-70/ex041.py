# DESAFIO: A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: -Até 9 anos: MIRIM. -Até 14 anos: INFANTIL. -Até 19 anos: JUNIOR. -Até 25 anos: SÊNIOR. -Acima: MASTER.

from datetime import date
nascimento = int(input('Em que ano você nasceu?: '))
idade = date.today().year - nascimento
if idade <= 9:
    print(
        f' Você esta na categoria: MIRIM. ')
elif idade <= 14:
    print(
        f' Você esta na categoria: INFANTIL. ')
elif idade < 19:
    print(
        f' Você esta na categoria: JUNIOR. ')
elif idade <= 25:
    print(
        f' Você esta na categoria: SÊNIOR. ')
else:
    print(
        f' Você esta na categoria: MASTER. ')

# #OUTRA MANEIRA
# from datetime import date
# nascimento = int(input('Em que ano você nasceu?: '))
# idade = date.today().year - nascimento
# if idade <= 9:
#     print(
#         f' Você esta na categoria: MIRIM. ')
# elif idade > 9 and idade <= 14:
#     print(
#         f' Você esta na categoria: INFANTIL. ')
# elif idade > 14 and idade < 19:
#     print(
#         f' Você esta na categoria: JUNIOR. ')
# elif idade > 19 and idade <= 20:
#     print(
#         f' Você esta na categoria: SÊNIOR. ')
# else:
#     print(
#         f' Você esta na categoria: MASTER. ')
