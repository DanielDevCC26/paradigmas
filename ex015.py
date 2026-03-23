'''prog que pergunte os km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.'''

distance = float(input('Quantos km você percorreu com o carro? '))
days = int(input('Quantos dias você ficou com o carro? '))
cost_distance = distance*0.15
cost_days = days*60
sum = cost_days+cost_distance
print('Você percorreu {}km, em {} dias. O custo de diárias foi de R${} e de quilometragem foi de R${}. \nTotalizando R${:.2f}'.format(distance, days, cost_days, cost_distance, sum))