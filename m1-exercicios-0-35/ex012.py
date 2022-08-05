# DESAIO: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto?: R$'))
desconto = float(input('Qual o valor do desconto?: %'))
desconto = desconto / 100
vd = preço * desconto
vf = preço - vd

print(f'Valor original: R${preço}')
print(f'Desconto ganho: R${vd:.2f}')
print(f'O valor com desconto é de: R${vf:.2f}')
