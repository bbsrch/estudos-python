# Função leiaint() que é um 'input' e só aceita valor numérico

def leiaint(num):
    while True:
        n = input(num)
        if n.isnumeric():
            return n
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m')


aoba = leiaint('Digite um número: ')
print(f'Você digitou o número {aoba}.')