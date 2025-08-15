# Matriz usando listas

# Minha resolução:
coluna = []
li1 = []
li2 = []
li3 = []
soma = 0
for l in range(1, 4):
    for c in range(1, 4):
        coluna.append(int(input(f'Digite um valor para [{l}, {c}]: ')))
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

# Resolução do professor:
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
"""
