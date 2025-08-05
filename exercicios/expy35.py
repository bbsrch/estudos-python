# um programa que diz se três retas podem formar um triângulo
l1 = float(input('digite o comprimento da primeira reta: '))
l2 = float(input('digite o comprimento da segunda reta: '))
l3 = float(input('digite o comprimento da terceira reta: '))
if (l1 - l2) < l3 < (l1 + l2):
    print('É possível formar um triângulo.')
else:
    print('Não dá para formar um triângulo.')