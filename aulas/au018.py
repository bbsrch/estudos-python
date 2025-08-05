# Listas v2
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('-='*20)

pessoas = [['Andrew', 19], ['Hunter', 21], ['João', 45], ['Camila', 33]]
print(pessoas)
print(pessoas[1])
print(pessoas[1][0])

print('-='*20)

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-=' * 20)

povo = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')).capitalize())
    dado.append(int(input('Idade: ')))
    povo.append(dado[:])
    dado.clear()
print(povo)

for p in povo:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')