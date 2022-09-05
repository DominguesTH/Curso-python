# DEASFIO: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo nome e idade em um arquivo de texto simples. O sistema só vai ter  2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from time import sleep
from uteis.interface import *
from uteis.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        LerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        sleep(1)
        cabeçalho('      \033[0;36mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[0;31m ERRO! Digite uma opcão válida! \033[m')
    sleep(2)
