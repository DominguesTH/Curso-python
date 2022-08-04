# DESAFIO: Faça um programa que leia a largura e a altura de uma parede em metro e calcule a sua área e a quantidade de tinta necessário para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m².

lp = float(input('Qual a largura da parede?: '))
ap = float(input('Qual a altura da parede?: '))
area = ap * lp
print(
    f' As dimensões da parede são {lp}x{ap} e sua área é de {area}m². \n Considerando que cada litro de tinta pinta 2m², será necessário {area/2:.3f}l de tinta para pintar toda a parede.')
