# Função fatorial() que dá a opção de mostrar o cálculo e tem o docstring

def fatorial(n, show=False):
    """
    >> Essa função calcula o fatorial de um número.
    :param n: O número a ser fatorado.
    :param show: Mostrar ou não mostrar o cálculo
    :return: O valor do fatorial da variável 'n'
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f'O fatorial de {n} é {f}')
    if show:
        print(n, end=' ')
        for c in range(n-1, 0, -1):
            print(f'x {c}', end=' ')
        print('=', f)
    print('-='*20)
    return f


fatorial(5, show=True)
fatorial(6)
fatorial(7, show=True)
