'''#prog que leia o ano de nascimento de sete pessoas, 
no final, mostre quantas são maiores de idade e quantas são
menores de idade'''
from datetime import date

ano_atual = date.today().year

maiores = 0
menores = 0

for c in range (0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são maiores e {} pessoas são menores.'.format(maiores, menores))