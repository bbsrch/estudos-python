# Função que analisa qual o maior dos valores digitados
from time import sleep
def maior(*valores):
    for v in valores:
        print(v, end = ' ')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')
    print('-='*30)

maior(1,4,8,2,8,6,9)
maior(5,6,3,6,7,1)