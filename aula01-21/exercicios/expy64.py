# Um programa que soma vários números inteiros, encerra quando digitado '999'. No final mostra a contagem e a soma, sem o '999'
num = soma = cont = 0

while num != 999:
    num = int(input('Digite um valor ou 999 para sair: '))
    if num != 999:
        soma += num
        cont += 1
print('A soma de {} valor(es) digitado(s) é {}.'.format(cont, soma))