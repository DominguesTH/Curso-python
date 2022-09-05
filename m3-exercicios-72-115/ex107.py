# DESAFIO: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir() dobro() e metade().  Faça também um progranma que importe esse módulo e use algumas dessa funções.
from uteis import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é  R${moeda.metade(p)}')
print(f' O dobro de {p} é  R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13% temos R${moeda.diminuir(p,13)}')
