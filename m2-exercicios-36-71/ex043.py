# DESAFIO: Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: -Abaixo de 18.5: Abaixo do peso. -Entre 18.5 e 25: peso ideial. -25 até 30: Sobrepeso. -30 até 40: Obesidade. - Acima de 40: Obesidade mórbida.

peso = float(input('Qual é o seu peso em? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Peso ideial.')
elif imc > 25 and imc < 30:
    print('Sobrepeso.')
else:
    print('Obesidade mórbida')
print(f'Seu IMC de {imc:.1f}')
