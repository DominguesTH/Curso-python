# DESAFIO: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram difitados e qual foi a soma entre eles (desconsiderando o flag)

numero = soma = soma_numero = 0
while numero != 999:
    numero = int(input('Digite um valor: '))
    if numero != 999:
        soma_numero = numero + soma_numero
        soma += 1
print(f'O resultados da soma dos {soma} valores inseridos é de: {soma_numero}')
