# DESAFIO: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pergunta o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o valor do seu salário?: R$'))
anos = int(input('Em quantos anos você pretende pagar?: '))
prestação = casa / (anos * 12)
if prestação > salario - (salario * 70 / 100):
    print(
        f'Financimento NEGADO. As parcelas de R${prestação:.2f} são superiores a 30% do seu salário.')
else:
    print(
        f'Financiamento APROVADO! O valor das prestações ficaram em: R${prestação}')
