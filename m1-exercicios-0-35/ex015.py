# DESAFIO: Escreva um programa que pergunte a quantidade de Km percorrios por um carro a ligado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km.

dias = float(input('Quantos dias alugado?: '))
km = float(input('Quantos Kms foram percorridos?: '))
preço_dia = dias * 60
preço_km = km * 0.15
total = preço_dia + preço_km
print(f'O total a pagar é de: R${total}')
