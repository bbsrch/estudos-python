# Função que cria uma linha adaptável ao tamanho do texto
def escreva():
    txt = str(input('Digite algo: '))
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))

escreva()