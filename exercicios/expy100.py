# Uma função que sorteia números e outra que soma os pares
from random import randint
from time import sleep
def sorteia():
    for c in range(0,5):
        num.append(randint(1,10))
    print(f'Os valores sorteados foram: ', end = ' ')
    for c in num:
        print(f'[{c}]', end = ' ')
        sleep(0.5)
    print()


def somapar():
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares é {soma}')


num = list()
sorteia()
somapar()
