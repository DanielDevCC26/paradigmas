#prog que leia o ano de nascimento de um atleta e qual a categoria. até 9 mirim, até 14 infantil, até 19 junior, até 20 senior, acima master

from datetime import date

ano_de_nascimento = int(input('Qual ano você nasceu? '))
ano_atual = date.today().year 

idade = ano_atual - ano_de_nascimento

if idade <= 9:
  print('Você está na categoria MIRIM!')
elif idade <= 14:
  print('Você está na categoria INFANTIL!')
elif idade <= 19:
  print('Você está na categoria JUNIOR!')
elif idade <= 25:
  print('Você está na categoria SENIOR!')
else:
  print('Você está na categoria MASTER!')