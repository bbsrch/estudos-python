# Função ficha() que funciona mesmo que um dado não tenha sido informado

def ficha(a, b):
    if not a.isalnum():
        a = '<desconhecido>'
    if not b.isnumeric():
        b = '0'
    print(f'O jogador {a} fez {b} gols no campeonato.')


jogador = input('Nome do jogador: ')
gol = input('Gols: ')
ficha(jogador, gol)
