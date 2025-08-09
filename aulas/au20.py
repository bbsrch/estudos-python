# Funções v1
def linha():
    print('-'*30)

linha()
print('uauuu')
linha()
linha()
print('isso é muito mais fácil')
linha()

def titulo(msg):
    print('='*30)
    print(msg)
    print('='*30)

titulo('suco de maçã')

def soma(a, b):
    print(f'A={a} B={b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(1, 4)
linha()
soma(5, 6)
linha()

def contador(*num):
    print(f'Recebi os valores {num} e ao todo são {len(num)} números.')

contador(2, 1, 7)
contador(4, 5)
linha()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [3,6,4,8,1,5]
dobra(valores)
print(valores)
linha()

def somainf(*digit):
    s = 0
    for num in digit:
        s += num
    print(f'A soma dos valores é {s}')

somainf(1,2,3,4,5)
somainf(1,4,7)
somainf(2,4,3,7,5,7,6,5,4)