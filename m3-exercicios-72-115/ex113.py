# DESAFIO: Reescreva a função leiaInt() que fizemos no desafio 104, inlcuindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
print('-'*30)


def leiaInt(i):
    while True:
        try:
            a = int(input(i))
        except (ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31m Entrada de dados interropida pelo usuário.  \033[m')
            return 0
        else:
            return a


def leiaFloat(i):
    while True:
        try:
            a = float(input(i))
        except (ValueError, TypeError):
            print('\033[0;31m ERRO! Digite um número Real válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31m Entrada de dados interropida pelo usuário.  \033[m')
            return 0
        else:
            return a


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número Inteiro: ')
num = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {num}')
