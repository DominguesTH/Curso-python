# DESAFIO: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicioário se por acaso a CTPS for difretente de ZERO, o dicionario receberá tambem o ano de contratação e o salário. calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime, date
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - dados['idade']
dados['ctps'] = int(input('Carteira de trabalho (0 náo tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contração:  '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + \
        (dados['contratação'] + 35) - datetime.now().year
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
