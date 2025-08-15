# Modificação das funções para que elas tenham um parâmetro adicional para converter os valores no padrão do real brasileiro
from utilidadesCeV import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.real(n)} é {moeda.metade(n, True)}')     # 'True' significa que ela será convertida para o padrão brasileiro
print(f'O dobro de {moeda.real(n)} é {moeda.dobro(n, True)}')
print(f'Com aumento 10% temos {moeda.aumentar(n, 10)}')     # Perceba que aqui, onde não tem o 'True', ela é mostrada no formato padrão do Python
print(f'Com desconto de 7% temos {moeda.diminuir(n, 7, True)}')
