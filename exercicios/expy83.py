# Verificação de expressão válida, usando a contagem dos parênteses

# Minha primeira tentativa, achando que dava certo :p
"""exp = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('A expressão é valida!')
else:
    print('A expressão não é valida!')"""

# O objetivo desse sistema é não ter nada adicionado lista 'pilha', se tiver um '(' ou ')' sobrando, está errado
exp = str(input('Digite a expressão: '))
pilha = []
for sim in exp:
    if sim == '(':
        pilha.append(sim) # quando abre um parêntese, é inválido por enquanto
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop() # só valida quando fecha o parêntese que abriu
        else:
            pilha.append(')') # e se fechar parênteses antes de abri-lo, vai invalidar e parar a verificação
            break
if len(pilha) == 0:
    print('valida')
else:
    print('invalida')
