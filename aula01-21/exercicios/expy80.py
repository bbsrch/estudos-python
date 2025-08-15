# Criação de lista em ordem MANUALMENTE crescente
valores = list()
for c in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if c == 0:
        valores.append(num)
        print('Primeiro valor adicionado')
    elif num >= max(valores):
        valores.append(num)
        print('Valor adicionado ao final da lista')
    elif num <= min(valores):
        valores.insert(0, num)
        print('Valor adicionado na posição 0')
    elif valores[0] < num < valores[1]:
        valores.insert(1, num)
        print('Valor adicionado na posição 1')
    elif valores[1] < num < valores[2]:
        valores.insert(2, num)
        print('Valor adicionado na posição 2')
    elif valores[2] < num < valores[3]:
        valores.insert(3, num)
        print('Valor adicionado na posição 3')

print('-='*20)
print(f'Você digitou os valores {valores}')