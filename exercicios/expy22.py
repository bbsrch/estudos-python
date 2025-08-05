# mostra em maiúsculo, minúsculo, quantas letras no total(sem espaços)
# e quantas letras do primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())

print(nome.lower())

div = nome.split()
junto = ''.join(div)

print('seu nome completo tem {} letras'.format(len(junto)))

print('seu primeiro nome tem {} letras'.format(len(div[0])))