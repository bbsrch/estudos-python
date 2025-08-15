# Soma e contagem de números inteiros até digitar '999'
soma = cont = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores digitados é {soma}.')