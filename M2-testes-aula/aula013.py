# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM')


# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Pulo: '))
# if p <= 0:
#     print('Minímo 1, tente novamente.')
# else:
#     for c in range(i, f+1, p):
#         print(c)
# print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'O resultado da soma dos valores é de {s}')
