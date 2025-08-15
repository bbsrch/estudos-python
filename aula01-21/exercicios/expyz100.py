# Uma função que adiciona 5 números aleatórios numa lista e outra função que soma os pares
from random import randint
from time import sleep

def sorteia(lst):
    for c in range(0,5):
        lst.append(randint(1,10))
    print(f'Os valores sorteados foram:', end = ' ')
    for c in lst:
        print(f'[{c}]', end = ' ')
        sleep(0.5)
    print()

def somapar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares é {soma}')


num = list()
sorteia(num)
somapar(num)
