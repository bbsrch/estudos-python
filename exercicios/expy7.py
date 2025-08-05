# cálculo de média de notas
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m1 = (n1+n2)/2
if m1 >= 6.0:
    print('Essa é a média final: \033[32m{:.1f}\033[m'.format(m1))
else:
    print('Essa é a média final: \033[31m{:.1f}\033[m'.format(m1))