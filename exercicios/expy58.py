# Jogo de adivinhação v2.0

from random import randint
pc = randint(0, 10)
ten = 0

jogador = int(input('Estou pensando num número de 0 a 10. Tente adivinhar qual é!! '))
ten += 1
while jogador != pc:
    if jogador < pc:
        jogador = int(input('Mais... Tente novamente: '))
    else:
        jogador = int(input('Menos... Tente novamente: '))
    ten += 1

print('-=-'*20)
print('\033[36mVocê acertou\033[m o número {} na {}ª tentativa!'.format(pc, ten))
