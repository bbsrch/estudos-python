# Dá para formar um triângulo? Qual o tipo dele?
l1 = float(input('digite o comprimento da primeira reta: '))
l2 = float(input('digite o comprimento da segunda reta: '))
l3 = float(input('digite o comprimento da terceira reta: '))
print('-=-'*20)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('isósceles.')
    else:
        print('escaleno.')
else:
    print('Não dá para formar um triângulo.')