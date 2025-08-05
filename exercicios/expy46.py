# Contagem regressiva de 10 a 0 para lançar fogos de artifício com pausa a cada 1 segundo
from time import sleep

comando = int(input('Digite 1 para lançar os fogos!! '))
if comando == 1:
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('LANÇADOS...')
    sleep(1)
    print(';-;')
    sleep(1)
    print('\033[33mBOOOOOMMMMM!!!!!\033[m \033[31mPSHHHHHHHH!!\033[m \033[36mBAMMMMMMMMM!!!!!')
else:
    print('Lançamento abortado. Tente novamente.')