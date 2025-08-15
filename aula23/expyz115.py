# Crie um pequeno sistema modularizado que permita cadastrar pessoas em um arquivo de texto simples. O sistema só tem 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from mod115 import arquivo, geral

arq = 'pessoas.txt'
if not arquivo.existe(arq):
    arquivo.criar(arq)

while True:
    geral.calho('MENU PRINCIPAL', 1)    # Decidi colocar uma funcionalidade a mais na função, e agora dá para escolher a cor de fundo!!
    geral.op(1, 'Ver pessoas cadastradas')
    geral.op(2, 'Cadastrar nova pessoa')
    geral.op(3, 'Sair do sistema')
    op = geral.lerop('\033[36mSua opção: \033[m', 1, 3)     # Também adicionei outra funcionalidade que você escolhe o intervalo de valores aceitos como válido (ex: do 1 ao 3)
    if op == 1:
        geral.calho('PESSOAS CADASTRADAS', 32)
        arquivo.ler(arq)
    elif op == 2:
        geral.calho('NOVO CADASTRO', 36)
        nome = str(input('Nome: '))
        idade = geral.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif op == 3:
        geral.linha()
        print(f'{"Saindo do sistema...":^40}')
        geral.linha()
        break
