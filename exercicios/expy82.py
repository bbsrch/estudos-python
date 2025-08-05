# Criação de 2 listas de pares e ímpares a partir de uma original
lista = list()
pares = list()
impares = list()
while True:
    op = 'a'
    lista.append(int(input('Digite um valor: ')))
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    elif lista[c] % 2 == 1:
        impares.append(lista[c])
print(f'Lista completa: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')