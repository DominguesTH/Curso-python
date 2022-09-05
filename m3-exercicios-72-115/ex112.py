# DESAFIO: Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
from uteis import moeda

p = moeda.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 10)
