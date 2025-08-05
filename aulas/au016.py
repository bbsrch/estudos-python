# Tuplas
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita') # tupla, e também funciona sem ()
"""print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(lanche)
print(len(lanche))"""

print('~='*30)
for comida in lanche:
    print(f'Eu vou ingerir {comida}')
print('~='*30)
for cont in range(0, len(lanche)):
    print(f'Eu vou ingerir {lanche[cont]} na posição {cont}')
print('~='*30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou ingerir {comida} na posição {pos}')
print('~='*30)

print(sorted(lanche)) # ordem alfabética
print('~='*30)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c)) # comprimento da tupla
print(c.count(5)) # quantas vezes aparece o 5
print(c.index(5)) # em que posição está o primeiro 5
print(c.index(5, 2)) # em que posição tem o 5 depois do 2º caractere
print('~='*30)

pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa) # APAGA a tupla
print(pessoa)