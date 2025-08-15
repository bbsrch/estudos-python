# Nome, idade e sexo de 4 pessoas. Qual a média de idade? Quem é o homem mais velho? Quantas mulheres tem menos de 20 anos?
soma = 0
idadeM = 0
mulher = 0
velho = ''

for c in range(0, 4):
    print('===={}ª PESSOA===='.format(c+1))
    nome = input('Digite seu nome: ').strip().capitalize()
    idade = int(input('Digite sua idade: '))
    soma += idade
    sexo = input('Digite seu sexo (M/F): ').strip().upper()
    if sexo == 'M' and idade > idadeM:
        idadeM = idade
        velho = nome
    elif sexo == 'F' and idade < 20:
        mulher += 1
    print('-=-'*20)

media = soma / 4

print('A média de idade é {}, o homem mais velho é {} e há {} mulheres com menos de 20 anos.'.format(media, velho, mulher))