
# DESAFIO: Crie um proigrama que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


# print('='*30)
# print(' BANCO INTER')
# print('='*30)
# notas50 = notas20 = notas10 = notas1 = 0
# valor = int(input('Que valor você quer sacar? R$'))

# while True:
#     if valor >= 50:
#         valor -= 50
#         notas50 += 1
#     elif valor >= 20 or valor < 50:
#         valor -= 20
#         notas20 += 1
#     elif valor >= 10 or valor < 20:
#         valor -= 10
#         notas10 += 1
#     elif valor >= 1 or valor < 10:
#         valor -= 1
#         notas1 += 1
#     else:
#         if valor < 1:
#             print('ERRO! Impossivel sacar valores negativos')
#         if valor == 0:
#             break
# print('='*30)
# print(f'''Total de {notas50} cédulas de  R$50
# Total de {notas20} cédulas de R$20
# Total de {notas10} cédulas de R$10
# Total de {notas1} cédulas de R$1 ''')
# print('='*30)


# ===== CÓDIGO DO MESTRE =========

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DO CEV')
