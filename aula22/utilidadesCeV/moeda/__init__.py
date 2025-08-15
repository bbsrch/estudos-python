def aumentar(n, p, c=False):
    d = n + n * (p / 100)
    if c:
        r = f'R${d:.2f}'
        r = r.replace('.', ',')
        return r
    d = f'R${d}'
    return d

def diminuir(n, p, c=False):
    d = n - n * (p / 100)
    if c:
        r = f'R${d:.2f}'
        r = r.replace('.', ',')
        return r
    d = f'R${d}'
    return d

def dobro(n, c=False):
    d = n * 2
    if c:
        r = f'R${d:.2f}'
        r = r.replace('.', ',')
        return r
    d = f'R${d}'
    return d

def metade(n, c=False):
    d = n / 2
    if c:
        r = f'R${d:.2f}'
        r = r.replace('.', ',')
        return r
    d = f'R${d}'
    return d

def real(n):
    r = f'R${n:.2f}'
    r = r.replace('.', ',')
    return r

def resumo(a=0, b=0, c=0):
    """
    :param a: preço a ser analisado
    :param b: porcentagem do aumento
    :param c: porcentagem do desconto
    :return: uma tabela com várias informações sobre o valor
    """
    print('-'*30)
    print(f'\033[7m{'ANÁLISE DO VALOR':^30}\033[m')
    print('-'*30)
    print(f'Preço analisado:    {real(a)}')
    print(f'Dobro do preço:     {dobro(a, True)}')
    print(f'Metade do preço:    {metade(a, True)}')
    print(f'{b}% de aumento:     {aumentar(a, b, True)}')
    print(f'{c}% de desconto:    {diminuir(a, c, True)}')
    print('-'*30)
