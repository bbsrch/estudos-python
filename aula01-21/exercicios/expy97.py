# Função que cria uma linha adaptável ao tamanho do texto
def escreva(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)


escreva('Água mole em pedra dura, tanto bate até que fura.')
escreva('Cavalo dado não se olha os dentes.')
escreva('Good night!')