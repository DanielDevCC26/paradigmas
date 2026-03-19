#prog que pergunta preço da casa, salario, em quanto tempo vai pagar, parcela máxima 30% do salário

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Em quanto tempo pretende pagar? '))

prestação = valor / (tempo*12)
limite = salario*0.3

print('A parcela será de {:.2f}'.format(prestação))

if prestação > limite:
  print('Seu empréstimo foi negado')
else:
  print('Seu empréstimo foi aprovado!')