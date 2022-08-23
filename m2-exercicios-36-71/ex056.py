# DESAFIO: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: -A média de idade do grupo. -Qual é o nome do homem mais velho. -Quantas mulheres têm menos de 20 anos.
SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
nomevelho = ''
mulheres20 = 0
N_homens = 0
for p in range(1, 5):
    print('-'*5, f'{p}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    SomaIdade += idade
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if sexo == 'M':
        N_homens = + 1
    if p == 1 and sexo == 'M':
        MaiorIdadeHomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        nomevelho = nome


MediaIdade = SomaIdade / 4
print(f'A média de idade do grupo é de {MediaIdade:.2f} anos.')
if mulheres20 == 0:
    print('Não tem mulheres com menos de 20 anos na lista')
else:
    print(f'Ao todo são {mulheres20} mulheres com menos de 20 anos.')
if N_homens == 0:
    print('Não tem homens na lista.')
else:
    print(
        f'O homem mais velho tem: {MaiorIdadeHomem} anos e se chama {nomevelho}.')
