# Mini-calculadora
from time import sleep

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
print('-=-'*20)
op = 0
while op != 5:
    op = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA '''))
    print('-=-'*20)
    if op == 1:
        soma = num1 + num2
        print('A soma entre \033[31m{}\033[m e \033[31m{}\033[m é \033[32m{}\033[m'.format(num1, num2, soma))
    elif op == 2:
        x = num1 * num2
        print('A multiplicação entre \033[31m{}\033[m e \033[31m{}\033[m é \033[32m{}\033[m'.format(num1, num2, x))
    elif op == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        else:
            maior = 'nenhum. AMBOS SÃO IGUAIS.'
        print('O maior número é \033[32m{}\033[m'.format(maior))
    elif op == 4:
        print('Informe os números novamente.')
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))
    elif op == 5:
        print('Obrigado por usar este programa <3')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
print('fim.')