#prog que registra o ano de nasc de um jovem. se ainda não precisa alistar, se está na hora, ou se passou da hora.

from datetime import date

ano = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year

idade = ano_atual - ano

if idade < 18:
  print('Ainda falta tempo para se alistar.')
elif idade == 18:
  print('Está na hora de se alistar.')
else:
  print('Já passou da hora de se alistar.')