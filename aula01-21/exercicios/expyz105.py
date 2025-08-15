# Função notas(), com docstring, que calcula contagem, maior, menor, média e, opcionalmente, a situação da sala

def notas(*n, sit=False):
    """
    :param n: uma ou mais notas dos alunos
    :param sit: escolha se quer ver a situação da sala ou não
    :return: dicionário com várias informações sobre as notas digitadas
    """
    dic = dict()
    soma = 0
    dic['total'] = 0
    for nota in n:
        soma += nota
        dic['total'] += 1
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = soma / len(n)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['media'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    print(dic)


notas(7, 5.7, 10, 7, 10, sit=True)
