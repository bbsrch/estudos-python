# A frase é um palíndromo, desconsiderando os espaços?
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()    # dividiu a frase
junto = ''.join(palavras)   # juntou sem espaços
inverso = ''

for letra in range(len(junto)-1, -1, -1):   # ultima letra, até a primeira(0), descrescendo de um em um
    inverso += junto[letra]                 # soma letra da frase ao contrário, letra 19, letra 18, letra 17...
print('a frase invertida é:', inverso)
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

# inverso = junto[::-1] # podemos usar isso no lugar do 'for'