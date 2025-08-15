from time import sleep


def linha(tam=40):
    print('-' * tam)

def calho(txt, cor=0):
    linha()
    print(f'\033[7;{cor}m{txt.center(40)}\033[m')
    linha()

def op(n, txt):
    sleep(0.5)
    print(f'\033[33m{n} - \033[m', end="")
    print(f'\033[34m{txt}\033[m')

def lerop(txt, a, b):
    while True:
        try:
            linha()
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            sleep(1)
        except KeyboardInterrupt:
            print()
            print('\033[31mO usuário optou por não digitar um número\033[m')
            sleep(1)
            quit()
        else:
            if not n<b+1 or n<a:
                print('\033[31mErro! Digite uma opção válida.\033[m')
                sleep(1)
            else:
                return n

def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[31mO usuário optou por não digitar esse número\033[m')
            return 0
        else:
            return n