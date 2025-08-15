# Guardando informações de um aluno num dicionário
info = {'Nome': str(input('Nome do aluno: ')),
        'Média': float(input('Media do aluno: '))
}
print('-='*15)
if info['Média'] >= 7:
    info['Situação'] = 'aprovad@'
elif 5 <= info['Média'] < 7:
    info['Situação'] = 'recuperação'
else:
    info['Situação'] = 'reprovad@'
for k, v in info.items():
    print(f'{k} é {v}')