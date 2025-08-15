# Cálculo de área para proporção de tinta. Cada 2m² se usa 1 litro de tinta
l = float(input('qual a largura? '))
a = float(input('qual a altura? '))
ae = l*a
ti = ae/2
print('Sua área é de {}m² e você precisará de {} litros de tinta'.format(ae, ti))

