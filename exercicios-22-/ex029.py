# DESAFIO: Escreva um programa que leia a velocidade de um carro.  Se ele ultrapassar a 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
# =========Meu código================
vel = float(input('Qual a velocidade: '))
m = (vel - 80)*7
if vel > 80:
    print(f'Você foi multado no valor de R${m}')
else:
    print('Continue sempre respeitando o limite de velocidade. Boa viagem!')
