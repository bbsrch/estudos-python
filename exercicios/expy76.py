# Lista de preços
lista = ('Abacaxi', 8.00,
         'Maçã', 5.50,
         'Banana', 7.99,
         'Pera', 6.69,
         'Goiaba', 4.39)
print('-=-'*15)
print(f'{'LISTAGEM DE PREÇOS':^45}')
print('-=-'*15)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:5.2f}')