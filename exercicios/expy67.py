# Tabuada v3.0 com 'break'
while True:
    n = int(input('Digite um valor para ver a tabuada: '))
    print('-=-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-=-'*20)
print('Programa encerrado, volte sempre!')