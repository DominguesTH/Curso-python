# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoas em um dicionario e todos os dicionarios em uma lista. No final, mostre: A)Quantas pessoas foram cadastradas B)A média de idade do grupo. C) Uma lista com todas as mulheres. D)Uma lista com todas as pessoas com idade acima da média.

mulheres = list()
pessoas = list()
dados = dict()
somaidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    while True:
        dados['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
        if dados['sexo'] == 'F':
            mulheres.append(dados['nome'])
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    pessoas.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if continuar == 'N':
        break
media_idade = somaidade / len(pessoas)
print(f'-='*40)
print()
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas. ')
print(f'B) A média de idade foi de {media_idade:.1f} anos. ')
print(f'C) As mulhres encontradas foram {mulheres}')
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= media_idade:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=', ')
        print()
print()
print(f'-='*40)
print(F'<<ENCERRADO>>')
