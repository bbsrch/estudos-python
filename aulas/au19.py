# Dicionários

dados = {'nome':'Pedro', 'idade':'18'}
print(f'O {dados["nome"]} tem {dados["idade"]} anos.')
dados['sexo'] = 'Masculino' # Adiciona ou substitui uma variável no dicionário
print(dados['sexo'])
del dados['idade'] # Apagando uma variável
print(dados)

print('-='*20)

filme = {'título':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}
print(filme.values()) # Mostra os valores
print(filme.keys()) # Mostra os índices
print(filme.items()) # Mostra tudo
for k, v in filme.items():
    print(f'{k} = {v}')

print('-='*20)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print('-='*20)

fruta = dict()
alimento = list()
for c in range(0, 3):
    fruta['nome'] = str(input('Nome da fruta: '))
    fruta['gosto'] = str(input('Doce ou azedo: '))
    alimento.append(fruta.copy()) # cópia de dicionários
for f in alimento:
    print(f)
    for k, v in f.items():
        print(f'{k} = {v}')
