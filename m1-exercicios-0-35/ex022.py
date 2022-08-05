# DESAFIO: Crie um programa que leia o nome completo de uma pessoa mostre: -> O nome com todas as letras maiúsculas.  ->O nome com todas minúsculas. -> Quantas letras ao todo (sem considerar espaços). ->Quantas letras tem o primeiro nome.

# =========Meu código================
nome = str(input('Insira seu nome: '))
nome = nome.strip()
pnome = nome.split()
print(f' O nome: {nome} em maiúsculo é: {nome.upper()}')
print(f' Em minúsculo é: {nome.lower()}')
print(f' O nome completo tem {len(nome) - nome.count(" ")} letras')
print(f' E o seu primeiro nome tem {len(pnome[0])} letras ')


# # =========Código do Mestre================
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Analisando seu nome...')
# print(f'Seu nome em maiúsculo é {nome.upper()}')
# print(f'Seu nome em minúsculo é {nome.lower()}')
# print(f'Seu nome tem ao todo  {len(nome) - nome.count(" ")} letras.')
# print(f'Seu primeiro nome tem {nome.find(" ")} letras')


# print(
#     f' O nome: {nome} com as letras maiúsculas é: {nome.upper()} \n Com as letras minúsculo é: {nome.lower()} \n O nome completo tem {len(nome)} letras \n E o seu primeiro nome tem {len(pnome[0])} letras ')
