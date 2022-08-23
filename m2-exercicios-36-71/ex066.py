# DESAFIO: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o valor 999, que é a condição de para. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (Decosidere o flag.)

quantidade_numeros = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    quantidade_numeros += 1
print(f'A soma dos {quantidade_numeros} valores foi de {soma}!')

# #=== Outra forma que fiz sem usar o (TRUE) , ativei com a variavel no valor 0
# soma = cont = num = 0
# while num != 999:
#     num = int(input('Digite um valor (999 para parar): '))
#     if num == 999:
#         break
#     cont += 1
#     soma += num
# print(f'A soma dos {cont} valores foi de {soma}')
