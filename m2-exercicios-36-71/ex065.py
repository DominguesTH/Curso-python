# DESAFIO: Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# ======= MEU CÓDIGO CANSADO KKKKKK =======
# from time import sleep
# r = 'S'
# media_numero = soma_numero = n_inseridos = maior = 0
# menor = 999999
# while r == 'S':
#     n = int(input('Digite um número: '))
#     r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
#     soma_numero += n
#     n_inseridos += 1
#     if r == 'S':
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#     if r == 'N':
#         soma_numero += n
#         n_inseridos += 1
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
# if r == 'N':
#     print(f'---- Estamos encerrando o programa. Fique com seu resultado...  -----')
#     sleep(1.5)
# if r != 'S' and r != 'N':
#     print(f'---- Opção invalida. Vamos encerrar o programa.-----')
#     sleep(2)
# media_numero = soma_numero / n_inseridos
# print('='*50)
# print(
#     f'''----- O menor número inserido foi: {menor}
#   \n----- O maior foi: {maior}
#   \n----- A média dos números inserios é de {media_numero:.2f}''')
# print('='*50)

# ==== CÓDIGO DO MESTRE =====
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print(f'Você digitoi {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
