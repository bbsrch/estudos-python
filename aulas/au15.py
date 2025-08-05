# Interrupção
n = s = 0
while True:
    n = int(input('Digite um valor ou 999 para sair: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')

print('-=-'*20)

nome = 'José'
idade = 33
sal = 1983.4
print(f'O {nome} tem {idade} anos e ganha R${sal:.2f}.')