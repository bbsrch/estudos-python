# Tupla aleatória e ordenação
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {tupla}')

#ordem = sorted(tupla)
#print(f'O maior valor sorteado foi {ordem[-1]}')
#print(f'O menor valor sorteado foi {ordem[0]}')

print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')