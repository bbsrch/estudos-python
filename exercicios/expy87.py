# Análise da matriz

# Minha resolução:
coluna = []
li1 = []
li2 = []
li3 = []
soma = 0
soma2 = 0
for l in range(1, 4):
    for c in range(1, 4):
        coluna.append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if coluna[0] % 2 == 0:
            soma += coluna[0]
        if c == 3:
            soma2 += coluna[0]
        if l == 1:
            li1.append(coluna[:])
        elif l == 2:
            li2.append(coluna[:])
        elif l == 3:
            li3.append(coluna[:])
        coluna.clear()

print(li1[0], li1[1], li1[2])
print(li2[0], li2[1], li2[2])
print(li3[0], li3[1], li3[2])
print('-='*20)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da 3ª coluna é {soma2}')
print(f'O maior valor da 2ª linha é {max(li2)}')

# Resolução do professor:
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
"""
