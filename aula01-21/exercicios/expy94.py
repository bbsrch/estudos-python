# Análise aprimorada de dados com verificação instantânea de dados
lista = []
dic = {}
soma = 0
while True:
    sexo = 'a'
    op = 'a'
    dic['nome'] = str(input('Nome: ')).strip().capitalize()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('ERRO! Digite apenas M ou F.')
    dic['sexo'] = sexo
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    lista.append(dic.copy())
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if op not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if op == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'[{lista[c]["nome"]}]', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for c in (0, len(lista)):
    if lista[c]['idade'] > media:
        print(f'{lista[c]}')
print('<< ENCERRADO >>')
