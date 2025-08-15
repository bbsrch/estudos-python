# Análise de tupla
time = ('Cruzeiro','Flamengo','RB Bragantino','Palmeiras',
        'Botafogo','Bahia','Mirassol','Fluminense',
        'Atlético-MG','Corinthians','Ceará','Internacional',
        'Grêmio','São Paulo','Vitória','Vasco da Gama',
        'Santos','Juventude','Fortaleza EC','Sport Recife')

print(f'Times do Brasileirão em pontuação: {time}')
print('~='*50)
print(f'Os 5 primeiros colocados são {time[:5]}')
print('~='*50)
print(f'Os 4 últimos colocados são {time[-4:]}')
print('~='*50)
print(f'Ordem alfabética: {sorted(time)}')
print('~='*50)
print(f'O Fluminense está na posição: {time.index('Fluminense')+1}')