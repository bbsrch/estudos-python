# Analisa o peso de 5 pessoas e diz quem é mais obeso e quem é o esqueleto do grupo

# peso = float(input('Digite o peso da 1ª pessoa: '))       # Eu dividi o peso da primeira pessoa da repetição manualmente
pesado = 0
leve = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso < leve:
            leve = peso
        elif peso > pesado:
            pesado = peso


print('O mais pesado tem {}kg e o mais leve tem {}kg'.format(pesado, leve))