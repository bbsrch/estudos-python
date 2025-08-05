# separação dos números em sua respectiva casa
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10     # 9385 // 1 = 9385 // 10 = 938 e sobra 5(unidade)
d = num // 10 % 10    # 9385 // 10 = 938 // 10 = 93 e sobra 8(dezena)
c = num // 100 % 10   # 9385 // 100 = 93 // 10 = 9 e sobra 3(centena)
m = num // 1000 % 10  # 9384 // 1000 = 9 // 10 = 0 e sobra 9(milhar)

print('''unidade: {}
dezena: {}
centena: {}
milhar: {}'''.format(u, d, c, m))
