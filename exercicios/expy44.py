# Formas de pagamento diversas
valor = float(input('Qual o valor do produto? R$'))
print('''Qual a forma de pagamento?
[1] À vista no dinheiro ou cheque com 10% de desconto
[2] À vista no cartão com 5% de desconto
[3] 2x no cartão de crédito
[4] 3x ou mais no cartão de crédito com juros de 20% ''')
paga = int(input('Qual a forma de pagamento? '))
print('-=-'*20)
if paga == 1:
    print('O valor para pagamento com 10% de desconto fica R${:.2f}'.format(valor*0.90))
elif paga == 2:
    print('O valor para pagamento com 5% de desconto fica R${:.2f}'.format(valor*0.95))
elif paga == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(valor/2))
elif paga == 4:
    juros = valor * 1.20
    par = int(input('Quantas parcelas? '))
    print('Sua compra com juros de 20% ficará R${:.2f} e será parcelada em {}x de R${:.2f}'.format(juros, par, juros / par))
