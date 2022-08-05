# DESAFIO: Desenvolva um programa que pergunte a distâcia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

# =========Meu código================
km = float(input('Qual a distancia da viagem em km: '))
if km < 200:
    print(f'O valor da sua viagem é: R${km*0.50:.2f}')
else:
    print(f'O valor da viagem é: R${km*0.45:.2f}')
