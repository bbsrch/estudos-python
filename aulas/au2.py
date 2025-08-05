# Funções aritméticas

nome = input('qual é o seu nome? ')
print('prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
e = n1 ** n2

print('Soma: {},\n Subtração: {},\n Multiplicação: {},\n Divisão: {},\n Divisão inteira: {},\n Resto da divisão {},\n Exponenciação: {}'.format(s, su, m, d, di, re, e))
