# Placar de jogadores com análise individual
from time import sleep
dados = []
jogador = {}
gol = []
while True:
    op = 'a'
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    pt = int(input('Quantas partidas ele jogou? '))
    for c in range(0, pt):
        gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    dados.append(jogador.copy())
    gol.clear()
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if op not in 'SN':
            print('Erro! Digite apenas S ou N.')
    if op == 'N':
        break
print('-='*30)
print('cod', end = ' ')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
print('-'*40)
for k, v in enumerate(dados):
    print(f'{k:<3} ', end = "")
    for d in v.values():
        print(f'{str(d):<15}', end = "")
    print()
print('-'*40)
while True:
    op = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if op == 999:
        break
    if 0 <= op <= len(dados)-1:
        print(f'Levantamento do jogador {dados[op]['nome']}:')
        for c in range(0, len(dados[op]['gols'])):
            sleep(0.5)
            print(f'    No jogo {c+1} fez {dados[op]['gols'][c]} gols.')
    print('-'*40)
