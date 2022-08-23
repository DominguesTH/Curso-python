# DESAFIO: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: -À vista dinheiro/cheque: 10% de desconto. -À vista no cartão:5% de desconto. -Em até 2x no cartão: preço normal. -3x ou mais no cartão: 20% de juros.

print('='*5, "TABELA DE DESCONTOS", '='*5)
print('-'*5, "À vista dinheiro/cheque desconto de: 10%", '-'*5)
print('-'*5, "À vista no cartão desconto de: 5%", '-'*5)
print('-'*5, "Até 2x sem juros", '-'*5)
print('-'*5, "Acima de 3x juros de: 20%", '-'*5)
print('='*31)

preço = float(input(' Qual é o preço do produto? R$'))
condição = int(
    input(''' Qual a condição de pagamento?
     [1] À vista dinheiro/cheque 
     [2] À vista cartão 
     [3] 2x no cartão 
     [4] 3x ou mais
     
     Digite um opção de "1 á 4": '''))
if condição == 1:
    total = preço - (preço * 10 / 100)
    print(
        f'Nessas condições você tem um desconto de 10% e o valor total a pagar fica em: R${total:.2f}')
elif condição == 2:
    total = preço - (preço * 5 / 100)
    print(
        f'Nessas condições você tem um desconto de 5% e o valor total a pagar fica em: R${total:.2f}')
elif condição == 3:
    nparcelas = 2
    vparcela = preço / nparcelas
    print(
        f'Sem juros nessas condições. Parcelado em {nparcelas}x de R${vparcela}, valor total R${preço}')
elif condição == 4:
    nparcelas = int(input('Qual o número de parcelas?: '))
    if nparcelas >= 3:
        total = preço + (preço * 20 / 100)
        vparcela = total / nparcelas
        print(
            f'Sua compra será parcelada em {nparcelas}x de R${vparcela:.2f} o juros será de 20% e o preço total ficará em: R${total:.2f}')
    else:
        print('Tente novamente. Mínimo de 3 parcelas para essa condição.')
else:
    print('Digite uma opção válida!')
