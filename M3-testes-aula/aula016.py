# # ===TUPLAS=====
# --> pode usar com () ou sem ()
lanches = 'Hamburguer', 'Lanche', 'Pizza', 'Pudim'

for comida in lanches:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posição {cont} ')

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba! ')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))  # --> Quantas vezes aparece o número 5
print(c.index(8))  # --> Em que posição esta o 8

# -- É possivel colocar varios tipos de dados diferentes em uma tupla
pessoa = ('Thiago', 27, 'M', 70.5)
del(pessoa)  # --> Sabendo que as tuplas são imutaveis, a única coisa que é possivel fazer caso seja necessario é deletar a tupla
print(pessoa)
