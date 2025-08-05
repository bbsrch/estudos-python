# Classificação de nadadores por categoria
ano = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano
print('Você tem {} ano(s).'.format(idade))
if idade <= 9:
    print('MIRIM!')
elif idade <= 14:
    print('INFANTIL!')
elif idade <= 19:
    print('JÚNIOR!')
elif idade <= 25:
    print('SÊNIOR!')
else:
    print('MASTER!')