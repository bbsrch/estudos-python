# Caixa eletrônico que mostra quais e quantas cédulas serão sacadas
from time import sleep
print('~=' * 20)
print('{:>25}'.format('BANCO ABDAR'))
cin = vinte = dez = um = 0

print('~=' * 20)
sleep(1)
print('Neste caixa há cédulas de R$50, R$20, R$10 e R$1.')
sleep(1)
saque = int(input('Digite o valor do seu saque: R$'))

while True:
    if saque >= 50:
        cin = saque // 50
        saque -= cin * 50
    elif saque >= 20:
        vinte = saque // 20
        saque -= vinte * 20
    elif saque >= 10:
        dez = saque // 10
        saque -= dez * 10
    elif saque >= 1:
        um = saque // 1
        saque -= um * 1
    elif saque == 0:
        break

print('~=' * 20)
print('PROCESSANDO SAQUE...')
print('~=' * 20)
sleep(2)
print(f'SAQUE REALIZADO:')
sleep(1)
print(f'\033[35m{cin}\033[m cédula(s) de R$50')
sleep(1)
print(f'\033[33m{vinte}\033[m cédula(s) de R$20')
sleep(1)
print(f'\033[31m{dez}\033[m cédula(s) de R$10')
sleep(1)
print(f'\033[32m{um}\033[m cédula(s) de R$1''')
sleep(1)
print('~=' * 20)
print('Obrigado por usar o BANCO ABDAR!')
