info = input('Digite algo: ')
print('É Alfabeto?: ', info.isalpha())
print('É um número?: ', info.isnumeric())
print('É um decimal?: ', info.isdecimal())
print('Só tem espaço?: ', info.isspace())
print('É alfanúmerico?: ', info.isalnum())


print('O tipo de primitivo desse valor é', type(info))
