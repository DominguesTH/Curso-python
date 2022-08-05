# print('\033[0;30;41m Teste ')
# print('\033[4;33;44m Teste ')
# print('\033[0;35;43m Teste ')
# print('\033[0;30;42m Teste ')
# print('\033[0;30m Teste ')
# print('\033[7;30m Teste ')


nome = 'Thiago'
cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '\033[33m', 'pretoebranco': '\033[7;30m'}
print(
    f'Olá! muito praer em te conehcer {cores["pretoebranco"]}{nome}{cores["limpa"]}')
