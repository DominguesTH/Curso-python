# DESAFIO: Desenvolva um programaq ue leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input(' primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (11 - 1) * razão
for c in range(primeiro, décimo, razão):
    print(f'{c}', end=' → ')
print('ACABOU')
