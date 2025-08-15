# análise de idade para alistamento militar
from datetime import date

ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Você tem {} anos em {}.'.format(idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda vai se alistar...falta(m) {} ano(s).'.format(saldo))
    print('Seu alistamento será em {}.'.format(atual + saldo))
elif idade == 18:
    print('Tá na hora de se alistar!!!')
else:
    print('Já passou do prazo de alistamento há {} ano(s)!'.format(idade-18))
