# Tratamento de Erros e Exceções

# Exceções são erros que não ocorrem sempre
try:       # operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário não informou os dados!')
except Exception as erro:
    print(f'Erro inesperado: {erro.__cause__}')
else:      # se deu certo
    print(f'O resultado é {r:.2f}')
finally:   # no final
    print('Fim')