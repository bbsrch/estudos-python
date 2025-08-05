# Análise de peso com listas compostas

temp = []
prin = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Peso: ')))
    if len(prin) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if resp == 'N':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {len(prin)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de', end=' ')
for p in prin:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de', end=' ')
for p in prin:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')