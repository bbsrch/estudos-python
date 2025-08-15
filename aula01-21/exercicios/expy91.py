# Jogando dados e ranqueando as jogadas
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'J1': randint(1, 6),
             'J2': randint(1, 6),
             'J3': randint(1, 6),
             'J4': randint(1, 6)}

print('JOGANDO OS DADOS...')
sleep(1)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*10)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

