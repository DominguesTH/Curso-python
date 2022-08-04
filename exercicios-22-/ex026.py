# DESAFIO: Faça um programa que leia uma frase pelo teclado e mostre: -> Quantas vezes aparece a letra "A". -> Em que posição ela aparece a primeira vez. ->Em que posição ela aparece a última vez.

# =========Meu código================
frase = str(input('Escreva uma frase: ')).upper().strip()
print(f'Na frase que você inseriu tem {frase.count("A")} letras A ')
print(f'A primeira vez que a letra "A" apareceu foi {frase.find("A")+1}')
print(f'A última letra "A" apareceu na posição {frase.rfind("A")+1}')
