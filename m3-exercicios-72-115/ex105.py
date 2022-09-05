# DESAFIO: Faça um programa que tenha uma função notas() que pode receber várioas notas de alunos e vai retornar um dicionário com as seguintes informações: -Quantidade de notas   -A maior nota  -A menor nota   -A média da turma    -A situação (opcional)
print('-'*50)


def notas(*n, sit=False):
    """ -> Analisa as notas inseridas e retorna um dicionario
    :param *n: uma ou mais notas dos alunos (aceita vários)
    :param sit: (valor opcional) indica se deve ou não adicionar a situação
    :retur: dicionario com várioas informações sobre a situação da turma.
    """
    alunos = dict()
    num = (n)
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['media'] = sum(num) / len(num)
    if sit:
        if alunos['media'] <= 5:
            alunos['situação'] = 'RUIM'
        if alunos['media'] > 5:
            alunos['situação'] = 'RAZOÁVEL'
        if alunos['media'] >= 7:
            alunos['situação'] = 'ÓTIMO'
    return alunos


# PROGRAMA PRINCIPAL
resp = notas(9.5, 2.5, 5.5,)
print(resp)
print()
# # AJUDA
# help(notas)
