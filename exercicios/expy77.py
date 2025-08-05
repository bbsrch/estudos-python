# Separação das vogais
palavras = ('CELULAR','MESA','CORTINA','COMPUTADOR','CONTROLE','TAPETE','CASA','PLANTA')
for c in palavras:
    print(f'\nNa palavra {c}, temos as vogais: ', end = '')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
