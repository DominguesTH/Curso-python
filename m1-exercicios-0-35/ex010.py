# DESAFIO: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$1,00 = R$3,27)

real = float(input('Quantos Reais você tem na carteira? R$'))
doll = real / 5.18
eur = real / 5.29
print(
    f'Com R${real} você conseguiria comprar: US${doll:.2f} ou €{eur:.2f}')
