# DESAFIO: Desenvolva um programa que leia as duas notas de um aluno,  calcule  e mostre a sua média.

n1 = float(input('Quanto foi a primeira nota?: '))
n2 = float(input('Quanto foi a segunda nota?: '))
# qtd_notas = len(n1, n2)
res = (n1 + n2) / 2

print(f'A média entre as notas é de {res:.2f} ')
