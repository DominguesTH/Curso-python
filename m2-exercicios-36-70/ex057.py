# DESAFIO: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# #===== MEU CÓDIGO =====
# sexo = ''
# while sexo != 'F' and sexo != 'M':
#     sexo = str(input('Qual é o seu sexo? [M/F]: ')).upper().strip()[0]
#     if sexo == 'M' or sexo == 'F':
#         if sexo == 'M':
#             print('Você é do sexo masculino.')
#         if sexo == 'F':
#             print('Você é do sexo feminino.')
#     else:
#         print('Opção incorreta, tente novamente!')
# print('FIM')

# ===== CÓDIGO DO MESTRE =====
sexo = str(input('Informe seu seco [M/F]: '))
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, infrome seu  sexo: ')
               ).strip().upper()[0]
print(f'Sexo {sexo} resgistrado com sucesso')
