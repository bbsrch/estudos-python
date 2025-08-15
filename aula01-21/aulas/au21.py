# Funções v2

def soma(a, b, c=0):    # '=0' torna a variável 'c' opcional
    """> Essa função calcula a soma de 2 ou 3 valores digitados.
    parâmetro a: primeiro valor
    parâmetro b: segundo valor
    parâmetro c: terceiro valor, opcional"""    # isso é uma docstring e serve para explicar a função usando help()
    s = a + b + c
    return s    # pode ser usado para retornar o resultado para uma variável pré-determinada

help(soma)      # manual de ajuda de funções
r1 = soma(3, 2)     # o 's' vai retornar para a variável 'r1'
r2 = soma(3,2,10)
r3 = soma(5, 3)
print(f'Os resultados foram {r1}, {r2} e {r3}.')

print('-='*30)

def funcao():
    n1 = 4      # criou uma nova variável de escopo local (função)
    global n2   # a variável global vai ser puxada para dentro da função
    n2 = 8      # substituiu o valor da variável global
    print(f'n1 dentro vale {n1}')

n1 = 2      # variável global
n2 = 5      # variável global
funcao()
print(f'n1 fora vale {n1}')
print(f'n2 alterado pela função vale {n2}')

print('-='*30)

def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

n = int(input('Digite um número para calcular o fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados foram {f1}, {f2} e {f3}')

print('-='*30)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero para verificar se é par: '))
if par(num):
    print('é par')
else:
    print('é impar')