# Manipulação de texto
frase = 'Curso em video Python'
print(frase)

# fatiamento
print(frase[9:21]) # do caractere 9 até o 20
print(frase[9::2]) # do caractere 9 até o final pulando de 2 em 2
print(frase[:9]) # do começo até o caractere 8
print(frase[2:18:2]) # do caractere 2 até o 17 pulando de 2 em 2

# análise
print(len(frase)) # conta os caracteres totais
print(frase.count('o',0, 13)) # conta quantos 'o' minúsculos tem na 'frase' do caractere 0 ao 12
print(frase.find('deo')) # ele mostra em que posição COMEÇOU o 'deo', se encontrado
print('Curso' in frase) # diz se existe o trecho 'Curso' na 'frase'

# transformação
frase.replace('Python', 'Android') # vai substituir o 'Python' por 'Android'
frase.upper() # modifica todas as letras para maiúsculo
frase.lower() # modifica todas as letras para minúsculo
frase.capitalize() # apenas a primeira letra é maiúscula
frase.title() # toda a palavra da 'frase' começa em maiúscula
frase.strip() # remove os espaços do começo e do fim
frase.rstrip() # remove apenas os espaços do fim(direita da frase)
frase.lstrip() # remove os espaços do começo(esquerda da frase)

# divisão
frase.split() # vai dividir a frase nos espaços
'-'.join(frase) # junta as partes divididas da frase com o hífen

