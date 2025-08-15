# se a velocidade for acima de 80km/h, ele vai pagar 7 reais por cada km/h acima dos 80
v = float(input('Qual a velocidade do seu carro? '))
if v > 80:
    print('\033[31mVocê foi multado! Valor da multa: R${:.2f}\033[m'.format((v - 80)*7))
else:
    print('\33[36mVocê está na velocidade permitida! <3')