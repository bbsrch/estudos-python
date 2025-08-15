# escolhe aleatoriamente um aluno
import random
a1 = str(input('digite o nome do primero aluno: '))
a2 = str(input('digite o nome do segundo aluno: '))
a3 = str(input('digite o nome do terceiro aluno: '))
a4 = str(input('digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
print('x alunx escolhidx para apagar o quadro foi \033[34m{}'.format(random.choice(lista)))