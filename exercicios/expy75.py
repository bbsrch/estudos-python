# Análise de tupla v2.0
tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o ultimo valor: ')))
print('~='*30)
print(tupla)
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes.')
else:
    print('Não foi digitado o número 9.')
if 3 in tupla:
    print(f'O primeiro número 3 está na posição {tupla.index(3)+1}')
else:
    print('Não foi digitado o número 3.')
print('Os números pares são: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')