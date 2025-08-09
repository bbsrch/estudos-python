# Diferentes layouts de 'print' com dicionário
from time import sleep
jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
pt = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, pt):
    gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-='*20)
sleep(1)
print(jogador)
print('-='*20)
sleep(1)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
    sleep(0.5)
print('-='*20)
sleep(1)
print(f'O jogador {jogador["nome"]} jogou {pt} partidas.')
sleep(1)
for c in range(0, pt):
    print(f'   => Na partida {c+1}, fez {gol[c]} gols.')
    sleep(0.5)
sleep(0.5)
print(f'Foi um total de {jogador["total"]} gols.')