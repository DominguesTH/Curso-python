# DESAFIO: Adapte o código do desafoio 107, criando uma função adicional chamada moeda() que consida mostrar os valores como um valor monetário formatado.
from uteis import numeros

p = float(input('Digite o preço: R$'))
print(f'A metade de {numeros.moeda(p)} é  {numeros.moeda(numeros.metade(p))}')
print(f'O dobro de {numeros.moeda(p)} é  {numeros.moeda(numeros.dobro(p))}')
print(f'Aumentando 10%, temos {numeros.moeda(numeros.aumentar(p, 10))}')
print(f'Reduzindo 13% temos {numeros.moeda(numeros.diminuir(p,13))}')
