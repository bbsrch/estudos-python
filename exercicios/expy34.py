# cálculo de aumento do salário. Salários  acima de 1250 recebem 10%, abaixo ou igual recebe 15%
s = float(input('Digite o valor do salário para calcular o aumento: '))
if s > 1250.00:
    aumento = s * 1.10
else:
    aumento = s * 1.15
print('O salário com aumento ficará R${:.2f}'.format(aumento))
