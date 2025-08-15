# Interactive Help personalizado
from time import sleep

def linha():
    print('\033[m='*40)

def ajuda():
    linha()
    print('\033[1;7m--Sistema de ajuda interativa do Python--')
    print('Digite "Sair" ou "S" para sair.')
    linha()
    while True:
        com = str(input('\033[36mQUAL COMANDO QUE VOCÊ PRECISA DE AJUDA? > ')).strip().lower()
        linha()
        if com == 's' or com == 'sair':
            print('\033[1;7m<< FIM DO PROGRAMA :) >>\033[m')
            break
        if com.isalnum():
            print(f'\033[4;31mBuscando informações sobre "{com}"...')
            linha()
            sleep(2)
            print('\033[7;32m')
            help(com)
            linha()


ajuda()
