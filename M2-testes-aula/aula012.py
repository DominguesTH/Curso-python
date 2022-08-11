# ESTRUTURA CONDICIONAL ALINHADAS

nome = str(input('Qual é seu nome?: ')).upper().strip()
if nome == 'THIAGO':
    print('Que nome bonito!')
elif nome == 'GABRIEL' or nome == 'FERNANDO':
    print('Você é um bosta!')
elif nome in 'MANUELA ISABELA CAROL':
    print('O nome com certeza é de uma bela mulher!')
else:
    print('Seu nome é normalzão em...')
print(f'Tenha um ótimo dia {nome.capitalize()}')
