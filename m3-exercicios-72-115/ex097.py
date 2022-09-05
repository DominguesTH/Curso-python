# DESAFIO: Faça um progama que tenmha uma funcão chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.  Ex: escreva(Ólá, mundo!')    Saída:~~~~~~~~~Olá, Mundo!~~~~~~~~
def escreva(txt):
    t = len(txt) + 4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


escreva('Olá')
escreva('Estou ficando bom em python')
escreva('Quando terminar o curso vou seguir carreira com certeza nisso!')
