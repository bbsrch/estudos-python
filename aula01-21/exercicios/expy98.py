# Função de sequência numérica
from time import sleep
def linha():
    print('-='*20)

def contador():
    while True:
        i = int(input('Início: '))
        f = int(input('Fim: '))
        p = int(input('Passo: '))
        linha()
        if p == 0:  # Se o passo for 0, será automaticamente convertido para 1
            p = 1
        if p >= 0:
            print(f'Contagem de {i} até {f}, de {p} em {p}')
        elif p < 0:
            p = (p*(-2)) + p    # Conversão do 'p' para positivo
            print(f'Contagem de {i} até {f}, de {p} em {p}')    # Mostra o 'p' positivo na tela
            p = -p     # Conversão do 'p' para negativo novamente

        if i > f:   # Se o início for maior que o fim, então será decrescente
            if p > 0:
                p = -p  # Isso garante que o passo será sempre negativo, já que é decrescente
            for num in range(i, f-1, p):
                sleep(0.3)
                print(num, end=' ')
        elif i < f:     # Se o início for menor que o fim, então será crescente
            if p < 0:
                p = (p*(-2)) + p    # Isso garante que o passo será sempre positivo, para não dar erro na lógica
            for num in range(i, f+1, p):
                sleep(0.3)
                print(num, end=' ')
        else:
            print(i, end=' ')
        print()
        linha()


linha()
print('Contagem de 1 até 10, de 1 em 1')
for c in range(1,11):
    sleep(0.3)
    print(c, end = ' ')
print()
linha()
print('Contagem de 10 até 0, de 2 em 2')
for c in range(10,-1,-2):
    sleep(0.3)
    print(c, end = ' ')
print()
linha()
print('Agora é sua vez de personalizar a contagem!')
contador()
