# cálculo de aprovação de financiamento. O valor da parcela não pode exceder 30% do salário
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos vai pagar? '))
mes = anos*12
par = float(casa/mes)
print('''ANÁLISE:
    valor da casa: \033[31mR${:.2f}\033[m dividida em \033[32m{}\033[m parcelas de \033[36mR${:.2f}\033[m'''.format(casa, mes, par))
print('-=-'*20)
if par > (sal*0.30):
    print('\033[31mFINANCIAMENTO NEGADO\033[m, devido a parcela ser maior que 30%(R${:.2f}) do seu salário de R${:.2f}'''.format(sal*0.30, sal))
else:
    print('\033[32mFINANCIAMENTO APROVADO\033[m, devido a parcela ser menor que 30%(R${:.2f}) do seu salário de R${:.2f}'.format(sal*0.30, sal))
