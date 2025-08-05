# Um programa que lê o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos dessa PA
ter = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
decimo = ter + (10 - 1) * raz


for c in range(ter, decimo + raz, raz):
    print(c, end = '->')
print('fim')
