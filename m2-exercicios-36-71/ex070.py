# DESAFIO: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quanto produtos custam mais de R$1000. C) Qual é o nome do produto mais barato.


print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
totmil = totgasto = menor = cont = 0
mais_barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    totgasto += preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-'*30)
    if cont == 1 or preço < menor:
        menor = preço
        mais_barato = produto
    if preço > 1000:
        totmil += 1
    if continuar == 'N':
        break
print('-=-'*5, 'FIM DO PROGRAMA', '-=-'*5)
print(f'''O total da compra foi R${totgasto}
Temos {totmil} produtos custando mais de R$1000 
O produto mais barato foi {mais_barato} que custa R${menor:.2f}''')
