# DESAFIO: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as nostas de cada aluno individualmente

# from time import sleep
# lista = list()
# listemp = list()
# while True:
#     listemp.append(str(input('Nome: ')))
#     listemp.append(float(input('Nota 1: ')))
#     listemp.append(float(input('Nota 2: ')))
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     lista.append(listemp[:])
#     listemp.clear()
#     if continuar in 'N':
#         break
# print('=-' * 30)
# print('Nº', 'NOME',         'MÉDIA')
# print('-'*30)
# for l, n in enumerate(lista):
#     print(f'{l}  {n[0]} {sum(n[:][1:]) / 2}')
# print('-'*30)
# while True:
#     aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if aluno == 999:
#         break
#     if aluno > len(lista):
#         print('-' * 50)
#         print(f' ERRO! Indice inválido, escolha um númreo válido no índice ')
#         print('-' * 50)
#     else:
#         print('-' * 50)
#         print(
#             f'A notas do(a) aluno(a) {lista[aluno][0]} foram: {lista[aluno][1:]}')
#         print('-' * 50)
#         sleep(1)
# sleep(1)
# print('ENCERRADNO')
# sleep(1)
# print('FIM')


# # ===== AJUSTES MEU CÓDIGO ======
# from time import sleep
# lista = list()
# listemp = list()
# while True:
#     listemp.append(str(input('Nome: ')))
#     listemp.append(float(input('Nota 1: ')))
#     listemp.append(float(input('Nota 2: ')))
#     continuar = ' '
#     while continuar not in 'SN':
#         continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     lista.append(listemp[:])
#     listemp.clear()
#     if continuar in 'N':
#         break
# print('=-' * 30)
# print(F'{"Nº":<4}{"NOME":10}{"MÉDIA":>8}')
# print('-'*30)
# for l, n in enumerate(lista):
#     print(f'{l:<4}{n[0]:<10} {sum(n[:][1:]) / 2:>8.1f}')
# print('-'*30)
# while True:
#     aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if aluno == 999:
#         break
#     if aluno > len(lista):
#         print('-' * 50)
#         print(f' ERRO! Indice inválido, escolha um númreo válido no índice ')
#         print('-' * 50)
#     else:
#         print('-' * 50)
#         print(
#             f'A notas do(a) aluno(a) {lista[aluno][0]} foram: {lista[aluno][1:]}')
#         print('-' * 50)
#         sleep(1)
# sleep(1)
# print('ENCERRADNO')
# sleep(1)
# print('FIM')


# ===== CÓDIGO DO MESTRE ======
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
