# Progressão aritmética v3.0 que pergunta mais quantos termos o usuário quer ver, encerra quando for '0'
""" VERSÃO #1 MINHA, FUNCIONANTE, MAS ERRADA :\
print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
cont = 1
fim = int(input('Quantos termos você quer mostrar? '))
while cont <= fim:
    print('{} >> '.format(pt), end = '')
    pt += ra
    cont += 1
print('FIM')
"""

print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} >> '.format(pt), end = '')
        pt += ra
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
