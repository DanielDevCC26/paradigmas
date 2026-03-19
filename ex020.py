# o msm professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos. faça  um prog que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print('A ordem dos alunos será: ', lista)

