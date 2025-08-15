# Uma função chamada resumo() que é todas as funções criadas anteriormente, comprimidas em uma só
from utilidadesCeV import moeda

v = float(input('Digite o preço: R$'))
moeda.resumo(v, 80, 35)
help(moeda.resumo)
