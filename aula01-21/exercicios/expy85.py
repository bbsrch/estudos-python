# Pares e ímpares separados, numa lista só

# Como seria com mais de 1 lista:
"""
valores = []
par = []
impar = []
for c in range (1,8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
valores.append(par[:])
valores.append(impar[:])

print(f'Pares: {valores[0]}')
print(f'Ímpares: {valores[1]}')
"""

# Resolução final:
n = [[], []]
valores = 0
for c in range (1,8):
    valores = int(input('Digite um valor: '))
    if valores % 2 == 0:
        n[0].append(valores)
    else:
        n[1].append(valores)
n[0].sort()
n[1].sort()
print(f'Os valores pares: {n[0]}')
print(f'Os valores ímpares: {n[1]}')
