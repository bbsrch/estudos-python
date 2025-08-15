# Contagem de números na lista, ordem decrescente e análise do número 5
lista = list()
while True:
    op = 'a'
    lista.append(int(input('Digite um valor: ')))
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-='*20)
print(lista)
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 not in lista:
    print('O número 5 NÃO está na lista!')
else:
    print('O número 5 está na lista!')