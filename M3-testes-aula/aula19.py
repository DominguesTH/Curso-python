# Criando um dicionario
filme = {
    'titulo': 'Star wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}
print('-'*30)
# retorna os valores dentro da  key
print(filme.values())
# retorna as keys declaradas
print(filme.keys())
# retorna todo dicionario
print(filme.items())
# Usando 'for' para printar os itens do dicionario
for k, v in filme.items():
    print(f'{k} é {v}')
print('-'*30)
locadora = list()
locadora.append(filme)
print(locadora[0]['diretor'])
print('-'*30)

# ==== PRÁTICANDO NA AULA =====
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('-'*30)
for k in pessoas.keys():
    print(k)
print('-'*30)
for k in pessoas.values():
    print(k)
print('-'*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')


# ==== DICIONARIO DENTRO DE UMA LISTA =====
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print('-'*30)
print(estado2)
print('-'*30)
print(brasil)
print('-'*30)
print(brasil[1])
print('-'*30)
print(brasil[0]['UF'])
print('-'*30)

# -----------------
print('-'*30)
print('Dessa FORMA')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print('-'*30)
print('Dessa FORMA')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print('-'*30)
print('Dessa FORMA')
for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()
