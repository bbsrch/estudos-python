# Variáveis
n1 = int(input('digite um numero '))
n2 = int(input('digite outro numero '))
res = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale: {}!'.format(res))
print('A soma entre {} e {} vale {}!'.format(n1, n2, res))


n = input('digite algo ')
print('numérico?', n.isnumeric())
print('alfabético?', n.isalpha())
print('alfanumérico?', n.isalnum())
print('tudo maiúsculo?', n.isupper())
print('tudo minúsculo?', n.islower())
print('é um espaço?', n.isspace())
