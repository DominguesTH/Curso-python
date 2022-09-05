
def aumentar(v=0, p=0, form=False):
    d = v * (p / 100)
    r = v + d
    return r if form is False else moeda(r)


def diminuir(v=0, p=0, form=False):
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
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
