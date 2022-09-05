# ======= Emoji bugado ========
import random
from math import sqrt, floor
import math
from emoji import emojize
print(emojize('Olá mundo! :call_me_hand:'))
print(emojize("Olá mundo! :smile:", language='alias'))

# # ======= Raiz quadrada ========
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz} ')


# ======= Raiz arendonda para menos ========
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)} ')

# ======= Sortear número ========
num1 = int(input('Sortear de: '))
num2 = int(input('Até: '))
res = random.randint(num1, num2)
print(f'O número sorteado foi {res}')
