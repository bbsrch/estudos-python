# Módulos e pacotes
from uteis import numeros   # importei um pacote dentro de outro pacote que criei

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {numeros.fatorial(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')
