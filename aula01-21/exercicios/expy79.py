# Criação de lista com valores únicos, em ordem crescente
valores = list()
while True:
    op = 'a'
    num1 = int(input('Digite um valor: '))
    if num1 not in valores:
        valores.append(int(num1))
        print('\033[36mAdicionado com sucesso!\033[m')
    else:
        print(f'\033[31mValor {num1} já cadastrado!\033[m')
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('-='*20)
print(sorted(valores))