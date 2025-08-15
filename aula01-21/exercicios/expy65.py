# Um programa que lê quantos números o usuário quiser, no final mostra a média, menor e o maior número digitado
soma = cont = maior = menor = 0
op = 'S'

while op == 'S':
        num = int(input('Digite um valor: '))
        soma += num
        cont += 1
        if cont == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()
        while op != 'N' and op != 'S':
            print('Comando inválido. Tente novamente.')
            op = str(input('Deseja continuar? [S/N] ')).strip().upper()

else:
    print('-=-'*20)
    media = soma / cont
    print('''VALORES DIGITADOS: {}
MÉDIA: {:.2f}
MAIOR: {}
MENOR: {}'''.format(cont, media, maior, menor))
