# Cálculo de fatorial (sem usar o 'math'!!!!)
""" VERSÃO #1 COM MATH
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = (factorial(n))
print('O fatorial de {} é {}.'.format(n, f))"""


''' VERSÃO #2 DA MINHA CABECINHA
num = int(input('Digite um número para calcular o fatorial: '))
numg = num

if num <= 1:
    print('O fatorial de {} é {}.'.format(num, num))
else:
    multi = int(num - 1)
    while multi !=0:
        resu = int(num * multi)
        print('{} x {} = {}'.format(num, multi, resu))
        num = resu
        multi -= 1
    print('O fatorial de {} é {}.'.format(numg, num))
print('Programa encerrado :3')'''


# VERSÃO #3 DO PROFESSOR
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))








