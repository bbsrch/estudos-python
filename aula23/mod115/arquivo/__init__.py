from aula23.mod115 import geral
from time import sleep

def existe(txt):
    try:
        arq = open(txt, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar(txt):
    try:
        arq = open(txt, 'wt+')
        arq.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo {txt} criado com sucesso.')

def ler(txt):
    try:
        arq = open(txt, 'rt')
    except:
        print('Houve um erro ao ler o arquivo.')
    else:
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            sleep(0.7)
        arq.close()
        sleep(1)

def cadastrar(txt, nome='desconhecido', idade=0):
    try:
        arq = open(txt, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados no arquivo.')
        else:
            print(f'Dados de {nome} foram cadastrados com sucesso.')
            sleep(1)

