def aumentar(v=0, p=0, form=False):
    d = v * (p / 100)
    r = v + d
    return r if form is False else moeda(r)


def desconto(v=0, p=0, form=False):
    d = v * (p / 100)
    r = v - d
    return r if form is False else moeda(r)


def metade(n=0, form=False):
    n /= 2
    return n if not form else moeda(n)


def dobro(d=0, form=False):
    d *= 2
    return d if not form else moeda(d)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>7.2f}'.replace('.', ',')


def resumo(preço=0, taxa=5, taxades=10):
    print('-' * 30)
    print('RESUMO DO VALOR' .center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preço,taxa,True)}')
    print(f'{taxades}% de redução: \t{desconto(preço, taxades, True)}')
    print('-' * 30)


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(
                f'\033[0;31mERRO: \"{entrada}\" é um preço inválido! \033[m')
        else:
            valido = True
            return float(entrada)
