# Crie um módulo chamado 'moeda' que tenha as funções aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use a funções
from utilidadesCeV import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Com aumento 10% temos R${moeda.aumentar(n, 10)}')
print(f'Com desconto de 7% temos R${moeda.diminuir(n, 7)}')
