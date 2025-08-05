# Um programa que lê 6 números inteiros e apenas soma os que são pares
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos valores pares digitados é {}.'.format(soma))
