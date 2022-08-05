# DESAFIO: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.  Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# # =========Meu código================
# salario = float(input('Qual é o seu salário?: R$'))
# if salario > 1250:
#     print(
#         f'Você terá um aumento de R${salario * 0.10:.2f}, seu salário vai para R${(salario * 0.10) + salario:.2f}')
# else:
#     print(
#         f'Seu aumento será de R${salario * 0.15:.2f}, seu salário vai para R${(salario * 0.15) + salario:.2f}')


# =========Código do mestre================
salario = float(input(' Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f' Quem ganha R${salario:.2f} passa a ganhar R${novo:.2f}')


# # =========Teste de desconto================
# print('='*5, "TABELA DE DESCONTOS", '='*5)
# print('-'*5, "Até 2 itens desconto de: 5%", '-'*5)
# print('-'*5, "Acima de 3 itens desconto de: 10%", '-'*5)
# print('-'*5, "Acima de 6 itens desconto de: 15%", '-'*5)
# print('-'*5, "Acima de 10 itens desconto de: 25%", '-'*5)
# preço = float(input(' Qual é o preço do produto? R$'))
# qtd = float(input(' Quantos você vai levar?: '))
# if qtd <= 2:
#     preço = preço * qtd
#     novo = preço - (preço * 5 / 100)
# if qtd >= 3 and qtd <= 5:
#     preço = preço * qtd
#     novo = preço - (preço * 10 / 100)
# if qtd >= 6 and qtd <= 9:
#     preço = preço * qtd
#     novo = preço - (preço * 15 / 100)
# if qtd >= 10:
#     preço = preço * qtd
#     novo = preço - (preço * 25 / 100)
# print(
#     f'Comprando na quantidade de {qtd:.0f} itens, o preço total com desconto será de R${novo} ')
