# Função real() adicionada no módulo que é capaz de converter o número para melhor visualização do real brasileiro
from utilidadesCeV import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.real(n)} é {moeda.real(moeda.metade(n))}')
print(f'O dobro de {moeda.real(n)} é {moeda.real(moeda.dobro(n))}')
print(f'Com aumento 10% temos {moeda.real(moeda.aumentar(n, 10))}')
print(f'Com desconto de 7% temos {moeda.real(moeda.diminuir(n, 7))}')
