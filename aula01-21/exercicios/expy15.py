# cálculo de aluguel do carro. 60 reais por dia + 0,15 centavos por km rodado
d = int(input('quantos dias ele foi alugado? '))
km = float(input('quantos km ele rodou? '))
ca = d * 60 + km * 0.15
print('o valor total do aluguel será R${:.2f}!'.format(ca))