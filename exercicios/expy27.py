# leia o nome de uma pessoa e mostre o primeiro e o último nome
nome = str(input('Digite seu nome completo: ')).strip()
nomed = nome.split()
print('Seu primeiro nome é {}'.format(nomed[0]))
print('Seu último nome é {}'.format(nomed[-1])) # o -1 é o último item de uma lista, -2 é o penúltimo item e assim vai
