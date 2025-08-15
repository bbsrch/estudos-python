# Soma de todos os números impares que são múltiplos de 3 no intervalo de 1 a 500
soma = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
        cont += 1
print('A soma de todos os {} números impares múltiplos de 3 ficou: {}'.format(cont, soma))
