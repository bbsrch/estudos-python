# cálculo do comprimento da hipotenusa
import math
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))
qhi = co ** 2 + ca ** 2
# hi = qhi ** (1/2)
hi = math.sqrt(qhi)
print('o comprimento da hipotenusa é {:.2f}'.format(hi))

# hi = math.hypot(co, ca) # isso seria BEEEMMM mais fácil
