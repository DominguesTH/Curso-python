# DESAFIO: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chmado moeda e dado. Trasfira todas as funções utilizadas nos desafio 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from uteis import moeda

p = float(input('Digite o preço: '))
moeda.resumo(p, 20, 10)
