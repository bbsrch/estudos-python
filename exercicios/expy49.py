# Tabuada v2.0 usando o 'for'
tab = int(input('Digite um número para ver a tabuada: '))
print('-=-'*20)
for c in range(0, 11):
    print('{} x {} = {}'.format(tab, c, tab*c))
