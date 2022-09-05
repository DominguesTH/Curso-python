# Testes durante a aula no momento teorico.
from time import sleep


def contador(inicio, fim, passo):
    """-> Faz uma contagem e mostra na tela.
    :param inicio: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    Função criada por Thiago Domingues.
    """
    cont = inicio
    while cont <= fim:
        sleep(.5)
        print(f'{cont}', end='..', flush=True)
        cont += passo
    print('Fim')


contador(2, 10, 2)
help(contador)

# PARAMAMETROS OPCIONAIS - flexibiliza a incerção de dados na função


def somar(a=0, b=0, c=0):
    """-> Faz uma contagem e mostra na tela.
    :param inicio: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    Função criada por Thiago Domingues.
    """
    s = a + b + c
    print(f'{s}')


somar()

# ESCOPO DE VARIÁVEIS/ usando comando `global` para usar a variavel de dentro do escopo local.


def funcao(b):
    global a
    a = 8
    b += 2
    c = 2
    print(f'A adentro vale {a}')
    print(f'B adentro vale {b}')
    print(f'C adentro vale {c}')


a = 5
funcao(a)
print(f'A fora vale {a}')

# RETONANDO VALORES  (return)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')


# =========== PARTE PRATICA DA AULA =============
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


resp = par(int(input('Digite um número para saber se é par: ')))
print(resp)
if resp:
    print('É par!')
else:
    print('Não é par!')
