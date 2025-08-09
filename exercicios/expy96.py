# Função que calcula a área
def area():
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    area = a * b
    print(f'{a} x {b} equivale a {area}m².')

area()