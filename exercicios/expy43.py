# Calculadora de IMC
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
print('-=-'*20)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')