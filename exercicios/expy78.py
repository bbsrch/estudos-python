# Criação de lista, maior e menor
# MINHA VERSÃO
'''num = []
for c in range(0, 5):
    num.append(int(input(f"Digite o um valor para a posição {c}: ")))
print('-='*20)
print(num)
for p, v in enumerate(num):
    if v == max(num):
        print(f'O maior valor digitado foi {v} na posição {p}')
    elif v == min(num):
        print(f'O menor valor digitado foi {v} na posição {p}')
print('-='*20)'''


# VERSÃO DO PROFESSOR
num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f"Digite o um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(num)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()