# DESAFIO: Refaça o DESAFIO:35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: -Equilátero: todos os lados iguais. -Isósceles: dois lados iguais. -Escaleno: todos os lados diferentes.

print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os seguimentos acima não formam um triângulo')
