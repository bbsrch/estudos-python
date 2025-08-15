# Dados de uma pessoa, cálculo de idade e aposentadoria
from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).capitalize().strip()
ano = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-='*20)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}.')