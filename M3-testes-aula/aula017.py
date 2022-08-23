# LISTA DENTRO DE OUTRA LISTA
lista1 = ['Pedro', 25]
lista2 = ['Maria', 19]
lista3 = ['João', 32]
pessoas = []
pessoas.append(lista1[:])
pessoas.append(lista2[:])
pessoas.append(lista3[:])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
# mesma solução enxuta --------
lista1 = ['Pedro', 25]
lista2 = ['Maria', 19]
lista3 = ['João', 32]
pessoas = list([lista1[:], lista2[:], lista3[:]])
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])


# TESTE AULA
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
# Mesma estrutura, porém fazendo uma cópia dos dados sem criar uma relação entre as listas.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# 'FOR' NA LISTA
galera = [['João', 19], ['Ana', 33], ['Joaqiuim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')

# 'FOR' NA LISTA, com range para inputar varios dados do teclado na mesma lista sem criar relação
galera = list()
dados = list()
totmen = totmai = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
# Usando a mesma estrutura e adicionando outro 'for' para verificar a lista de idade e validar algum dado, no caso se a pessoa é maior de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1
print(
    f'Ao todo temos {totmai} pessoas maiores de idade, e {totmen} menores de idade.')
