# ---------------------Anotações aula--------------------------

# ========varias paradas kkkk============
frase = 'Curso em Vídeo Python'
print(frase[::2])


# ========Deixar maiúsculo============
frase = 'Curso em Vídeo Python'
print(frase.upper().count())

# ========Trocar nome============
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Poker'))


print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum""")

# ---------------------Minhas anotações--------------------------

# ========Sem variável============
name = str(input('Insira uma frase: '))
print(f'A frase inserida tem {len(name)} caracteres')

# ========Com variável============
name = str(input('Insira uma frase: '))
analise = len(name)
print(f'A franse inserida tem {analise} caracteres')

# ========Contatando determinada str============
frase = str(input('Insira uma frase: '))
letra = str(input(
    'Insira a letra que deseja saber a quantidade de vezes que ela se repete: '))
cnt = frase.count(letra)
print(f'A franse inserida tem {cnt} lentras {letra}')

# ========Deixa todo conteúdo da str em maiusculo============
frase = str(input('Insira uma frase: '))
print(f'A frase inserida ficara assim em maiúscula: {frase.upper()}')

# ========Remove os espaços do inicio e fim============
frase = str(input('Insira uma frase: '))
print(f'A frase inserida ficara assim em maiúscula: {frase.strip()}')

# ========Remove os espaços do inicio e fim============
frase = str(input('Insira uma frase: '))
print(f'A frase inserida ficara assim em maiúscula: {frase.split()}')
