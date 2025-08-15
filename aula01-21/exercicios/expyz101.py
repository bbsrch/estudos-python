# Função voto() para verificar é o voto é negado, facultativo ou obrigatório
from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos, você não pode votar.')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos, seu voto é facultativo.')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos, seu voto é obrigatório.')


a = int(input('Em que ano você nasceu? '))
voto(a)
