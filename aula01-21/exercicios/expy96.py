# Função que calcula a área
def area():
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    ar = a * b
    print(f'A área de um terreno {a} x {b} equivale a {ar}m².')


area()