# DESAFIO: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,mostre o conteúdo da estrutura na tela.

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif dados['media'] < 7 or dados['media'] >= 5:
    dados['situação'] = 'Recuperação'
elif dados['media'] < 5:
    dados['situação'] = 'Reprovado'
print('-='*50)
for k, v in dados.items():
    print(f' - {k} é igual a {v}')
