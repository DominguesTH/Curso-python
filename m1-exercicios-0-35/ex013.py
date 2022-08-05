# DESAFIO: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o seu salário?: R$'))
aumento = salario * 0.15
res = aumento + salario

print(f'O seu salário com 15% de aumento é de {res}')


# # Outra forma de fazer
# salario = float(input('Qual é o seu salário?: R$'))
# aumento = salario + (salario * 15 / 100)
# print(f'O seu salário com 15% de aumento é de R${aumento}')
