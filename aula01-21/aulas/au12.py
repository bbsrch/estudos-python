# Condições aninhadas
nome = str(input('digite seu nome: ')).strip().capitalize()
if nome == 'André':
    print('Que nome esbelto!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito comum no Brasil!')
elif nome in 'Hanter Camily Tainá Taina':
    print('Agora sim você vai sentir meu peido de verdade!')
else:
    print('Seu nome é muito medíocre!')
print('Tenha um bom dia {}'.format(nome))