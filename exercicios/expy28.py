# jogo de adivinhação de número
from random import randint
from time import sleep
n1 = randint(0, 5)
print('-=-'*20)
adv = int(input('Estou pensando num número de 0 a 5. Qual você acha que é? '))
print('*música de suspense*')
sleep(1)
if n1 == adv:
    print('-----\033[34mVocê venceu, eu também pensei no número {}!\033[m-----'.format(n1))
else:
    print('\033[31mVocê errou, eu pensei no número {} :(\033[m'.format(n1))
print('-=-'*20)