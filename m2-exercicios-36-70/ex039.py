# DESAFIO: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - se ele ainda vai se alistar ao serviço militar.  -Se é a hora de se alistar. - Se já passou do tempo do alistamento.  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nascimento = int(input('Em que ano você nasceu?: '))
idade = date.today().year - nascimento
if idade < 18:
    print(
        f'Você ainda é juvenil rapaz... Faltam {18 - idade} anos para para seu alistamento militar. ')
elif idade == 18:
    print(
        f'Você tem {idade} anos, esta é a idade correta para o alistamento militar. ')
elif idade > 18:
    print(
        f'Você tem {idade} anos, já passou do prazo de alistamento a {idade - 18} anos, vai da merda!')
