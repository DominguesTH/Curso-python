# tempo = int(input('Quantos anos tem seu carro?: '))
# if tempo <= 3:
#     print('Carro novo!')
# else:
#     print('Carro cansado')
# print('--FIM--')


# # #========Condição simplificada===========
# tempo = int(input('Quantos anos tem seu carro?: '))
# print('Carro novo!' if tempo <= 3 else 'Carro triste ;(')
# print('--FIM--')

# # #========Aula===========

# nome = str(input('Qual é o seu nome?: ')).lower()
# if nome == 'thiago':
#     print('Que nome lindo você tem!')
# else:
#     print('Nome bem comum...')
# print(f'Bom dia {nome.title()}!')

from operator import indexOf


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi de {m}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉS!')
else:
    print('Sua média ta um merda! Vai estudar e sai do celular!!')
