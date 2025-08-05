# cálculo do preço de uma viagem. 0,50 por cada km até 200km e 0,45 para viagens mais longas
km = float(input('qual a distância em km da viagem? '))
if km <= 200:
    print('Você pagará R${:.2f}'.format(km*0.50))
else:
    print('Você pagará R${:.2f}'.format(km*0.45))