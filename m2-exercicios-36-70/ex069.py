# DESAFIO: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrad, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:   A) Quantas pessoas tem mais de 18 anos.  B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.


print('-'*30)
print('CADASTRE UMA PESSOA')
mais18 = homens = Mmenor20 = 0
while True:
    print('-'*30)
    idade = int(input('Idade: '))
    continuar = sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*30)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        Mmenor20 += 1
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homens cadastrados
E temos {Mmenor20} mulheres com menos de 20 anos.  ''')
