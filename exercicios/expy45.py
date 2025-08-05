# Jokempô
from random import choice
from time import sleep

e1 = 'pedra'
e2 = 'papel'
e3 = 'tesoura'
jokempo = [e1, e2, e3]
jokempo2 = choice(jokempo)

jogador = str(input('pedra, papel ou tesoura? ')).strip().lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=-'*20)
if jogador == jokempo2:
    print('\033[33mEmpate!\033[m Eu também joguei {}.'.format(jokempo2))
elif jogador == 'pedra' and jokempo2 == 'tesoura' or jogador == 'papel' and jokempo2 == 'pedra' or jogador == 'tesoura' and jokempo2 == 'papel':
    print('\033[36mVocê ganhou!\033[m Eu joguei {}.'.format(jokempo2))
elif jogador == 'pedra' and jokempo2 == 'papel' or jogador == 'papel' and jokempo2 == 'tesoura' or jogador == 'tesoura' and jokempo2 == 'pedra':
    print('\033[31mVocê perdeu!\033[m Eu joguei {}.'.format(jokempo2))