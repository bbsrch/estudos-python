# Estrutura de repetição 'for'
com = int(input('Começo: ')) # escolha o começo, o fim e a ordem de uma sequência numérica
fim = int(input('Final: '))
ordem = int(input('Ordem: '))
for a in range(com, fim+1, ordem):
    print(a)

print('-=-'*20)

#for b in range(6, 0, -1):   # conta de 6 a 1 decrescendo(-1)
#    print(b)

print('-=-'*20)

#for c in range(0, 7, 2):    #  conta de 0 a 6 crescendo a cada 2
#    print(c)

s = 0
for d in range(0, 3):        # repetição de uma entrada de valor para soma
    n = int(input('Digite um valor: '))
    s += n                   # toda vez que "n" recebe um número, ele é adicionado à soma
print('A soma é:', s)
print('FIM')