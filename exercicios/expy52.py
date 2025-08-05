# Validação de números primos
tot = 0

num = int(input('Digite um número para análisar se é primo: '))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end = '') # se for divisível, fique azul
        tot += 1
    else:
        print('\033[31m', end = '') # senão, fique vermelho
    print(c, end = ' ')

print('\n\033[m', '-=-'*20)

if tot > 2:
    print('Ele foi dividido {} vezes e por isso ele NÃO é primo.'.format(tot))
else:
    print('Ele foi dividido apenas 2 vezes e por isso ele é primo.')
