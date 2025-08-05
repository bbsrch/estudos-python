# Dicionários

dados = {'nome':'Pedro', 'idade':'18'}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'Masculino' # Adicionando uma variável no dicionário
print(dados['sexo'])
del dados['idade'] # Apagando uma variável

print('-='*20)

filme = {'título':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}
print(filme.values()) # Mostra os valores
print(filme.keys()) # Mostra os índices
print(filme.items()) # Mostra tudo
for k, v in filme.items():
    print(f'O {k} é {v}')