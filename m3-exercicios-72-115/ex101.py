# DESAFIO: Crie um programa que tenha uma função chamada voto() que vai receber como parâmentro o ano de nascimento de uma pesoa , retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.


def voto(ano):
    from datetime import date
    ano = date.today().year - ano
    if ano >= 18 and ano < 65:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO. '
    elif ano < 16:
        return f'Com {ano} anos: NÃO VOTA.'
    elif ano >= 16 or ano >= 65:
        return f'Com {ano} anos: VOTO OPCIONAL. '


print('-'*30)
print(voto(int(input('Emm que ano você nasceu? '))))
