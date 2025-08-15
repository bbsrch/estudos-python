# Par ou ímpar, só interrompe quando o jogador perder
from random import randint

print('-=-'*20)
print('\033[36mPAR OU ÍMPAR\033[m')
print('-=-'*20)

cont = 0
while True:
    pc = randint(0, 10)
    n = int(input('Digite um número: '))
    soma = n + pc
    op = 'a'
    while op not in 'PI':
        op = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-=-'*20)
    if soma % 2 == 0:
        result ='PAR'
    else:
        result ='ÍMPAR'
    print(f'Você jogou {n} e o eu joguei {pc}. Total: {soma}, \033[31m{result}\033[m')
    print('-=-' * 20)
    if op == 'P' and result == 'ÍMPAR' or op == 'I' and result == 'PAR':
        break
    else:
        cont += 1
        print('Você ganhou! Vamos jogar novamente...')
        print('-=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')

