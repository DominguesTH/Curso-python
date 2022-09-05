# DESAFIO: Crie um programa que tenha a funç!ao leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas valor numérico. EX: n = leiaint('Digite um n')

print('-'*30)


def leiaint(i):
    from colorama import Fore, Style
    while True:
        a = (input(i))
        if a.isnumeric():
            return a
        else:
            print(Fore . RED, 'ERRO! Figite um número inteiro válido.',
                  Style.RESET_ALL)


# PROGRAMA PRINCIPAL
n = leiaint('Digite um número: ')
print(f'Vocë acabou de digitar o número {n}')
