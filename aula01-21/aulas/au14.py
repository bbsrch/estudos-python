# Estrutura de repetição 'while'
"""
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim') """

'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('fim') '''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor ou 0 para parar: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} ímpares.'.format(par, impar))