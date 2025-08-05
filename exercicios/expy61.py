# Progressão aritmética v2.0 usando 'while'
print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} >> '.format(pt), end = '')
    pt += ra
    cont += 1
print('FIM')
