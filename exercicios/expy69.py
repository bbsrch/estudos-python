# Análise demográfica usando 'while' e 'break'
adulto = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = 'a'
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]
    if idade > 18:
        adulto += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    op = 'a'
    while op not in "SN":
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        print('-=-'*20)
        break
    print('-=-' * 20)

print(f'''{adulto} pessoa(s) com mais de 18 anos
{homem} homem(s)
{mulher} mulher(es) com menos de 20 anos''')