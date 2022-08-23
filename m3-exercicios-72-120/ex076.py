# DESAFIO: Crie um programa que  tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, oraganizando os dados em forma tabular.
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99,
            'Mochila', 120.30,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<40}', f'R${listagem[pos + 1]:>7.2f}')
print('='*50)
