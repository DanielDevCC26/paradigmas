#prog que calculo aumento de salario, se for maior que 1250 o aumento é de 10%, se for menor é de 15%
salario = float(input('Qual o seu salário? R$'))
if salario <= 1250:
    novo = salario + (salario*15/100)
else: 
    novo = salario + (salario*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))