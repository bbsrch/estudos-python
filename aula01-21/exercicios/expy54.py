# Analisa o ano de nascimento de 7 pessoas e diz quantas são adultas ou não
from datetime import date

somac = 0
somaa = 0
atual = date.today().year

for c in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c+1)))
    idade = atual - ano
    if idade < 18:
        somac += 1
    else:
        somaa += 1
print('Há {} adulto(s) e {} menor(es) no grupo.'.format(somaa, somac))