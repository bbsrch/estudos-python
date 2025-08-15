# Função chamada leiadinheiro() no módulo 'dados' que é capaz de funcionar como input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários, até os digitados com ','
from utilidadesCeV import moeda, dados

v = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(v, 35, 22)
