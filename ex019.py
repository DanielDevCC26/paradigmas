# um prof quer sortear um dos seus quatro alunos para apagar o quadro. faça um prog que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

print('Aluno escolhido: ', random.choice([a1, a2, a3, a4]))