# Listas v1

# Adicionando
lista = ['chocolate','chiclete','pirulito']
print(lista)
lista.append('bala') # adicionei bala no final da lista
print(lista)
lista.insert(1,'bolacha') # adicionei bolacha na posição 1
print(lista)

print('-='*20)

# Removendo
lista.remove('chiclete') # removi o chiclete, ele remove o primeiro que aparecer
print(lista)
lista.pop(0) # popei para fora o que estava na posição 0: chocolate
print(lista)
lista.pop() # popei o último da lista
print(lista)
lista[1] = 'cenoura' # substituí o objeto que estava na posição 1 para 'cenoura'
print(lista)

print('-='*20)

valores = list(range(0,11,2)) # Criei uma lista chamada "valores" com números de 0 a 10 pulando a cada 2
print(valores)

print('-='*20)

# Ordens
valores2 = [4, 5, 1, 6, 2, 7]
valores2.sort() # Organiza em ordem alfabética ou crescente
print(valores2)
valores2.sort(reverse=True) # Organiza em ordem decrescente
print(valores2)

print('-='*20)

# Usuário adiciona manualmente frutas na lista
frutas = list()
for c in range(0,2):
    frutas.append(str(input('Digite uma fruta: ')).strip())
for p, v in enumerate(frutas):
    print(f'Na posição {p} encontrei a fruta {v}.')

print('-='*20)

# Ligação de lista
a = [1, 2, 3, 4, 5]
b = a # Liga as duas listas e qualquer alterações feitas
b[2] = 9 # coloca o 9 na posição 2 da lista 'b' e, também, da lista 'a' porque estão linkados com =
print(a)
print(b)

print('-='*20)

# Cópia de lista
doce = ['pudim','bolo','torta']
sweet = doce[:] # A lista 'sweet' é uma cópia da lista 'doce' e pode ser modificada individualmente
sweet[2] = 'pavê'
print(doce)
print(sweet)
