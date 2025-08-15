# Refaça a função leiaint() do exercício 104, incluindo a possibilidade de digitação de um tipo inválido usando o tratamento de erros. Faça o mesmo com leiafloat()

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

def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[31mO usuário optou por não digitar esse número\033[m')
            return 0
        else:
            return n


v = leiaint('Digite um número inteiro: ')
w = leiafloat('Agora digite um número real: ')
print(f'O número inteiro é {v} e o real é {w}')

