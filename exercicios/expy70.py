# Caixa registradora que soma o total da compra. Quantos produtos custam + de 1000 e qual o mais barato?
print('='*30)
print('LOJAS ABDAR')
total = mil = cont = menor = 0

while True:
    print('=' * 30)
    nome = str(input('Nome do produto: ')).strip().capitalize()
    valor = float(input('Valor do produto: R$'))
    total += valor
    cont += 1
    if cont == 1 or valor < menor:
        menor = valor
        menorp = nome
    if valor > 1000:
        mil += 1
    op = str(input('Deseja adicionar mais produtos? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
    elif op != 'S' and op != 'N':
        print('Opção inválida. Tente novamente.')
        op = str(input('Deseja adicionar mais produtos? [S/N] ')).strip().upper()[0]
print('-=-' * 20)
print(f'''O valor total da compra é \033[31mR${total:.2f}\033[m.
\033[31m{mil}\033[m produto(s) custam mais de R$1000 e o mais barato foi \033[36m{menorp}\033[m por \033[31mR${menor:.2f}\033[m.''')
