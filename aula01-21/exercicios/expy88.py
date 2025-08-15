# Jogos da mega-sena

# Minha resolução:
from random import randint
from time import sleep

jogo = []
num = []
print('='*30)
print('{:^30}'.format('MEGA-SENA'))
print('='*30)
op = int(input('Quantos jogos você deseja? '))
print(f'Sorteando {op} jogos...')
for c in range(0, op):
    for d in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in num:
                break
        num.append(n)
    jogo.append(num[:])
    jogo[c].sort()
    num.clear()
    sleep(0.7)
    print(f'Jogo {c+1}: {jogo[c]}')
sleep(1)
print('{:=^30}'.format('< BOA SORTE >'))

# Resolução do professor:
"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('     JOGA NA MEGA SENA      ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)
"""