# conversor de número inteiro para binário, octal e hexadecimal
num = int(input('Digite um número inteiro: '))
print('''Se você quer convertê-lo para:
binário, digite 1
octal, digite 2
hexadecimal, digite 3 ''')
conv = int(input('O que você quer? '))
print('-=-'*20)
if conv == 1:
    print('O número {} em \033[36mbinário\033[m é {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} em \033[31moctal\033[m é {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} em \033[33mhexadecimal\033[m é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
