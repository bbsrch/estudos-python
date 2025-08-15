# Só é permitido digitar M ou F

genero = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]
while genero != 'F' and genero != 'M':
    genero = str(input('Gênero inválido, tente novamente: ')).strip().upper()[0]

if genero == 'M':
    print('Você digitou masculino. Obrigado.')
if genero == 'F':
    print('Você digitou feminino. Obrigado.')