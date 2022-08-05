# DESAFIO: Façã um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ex: Ana Maria de Souza   primeiro: Ana. Último: Souza.

# =========Meu código================
from emoji import emojize
nome = str(input(' Qual seu nome completo?: '))
nome = nome.split()
print(emojize('É um prazer em te conhecer! :oncoming_fist:'))
print(f'Seu primeiro nome é {nome[0]} e o último é {nome[-1]} ')
