#prog que pergunta a distanci de uma viagem em km. calcula o preço da passagem, cobrando 0,50 por km para viagens de até 200km, e 0,45 para viagns mais longas
import math

distance = int(input('Qual a distancia percorrida na viagem?'))
viagem_curta = distance*0.50
viagem_longa = distance*0.45

if distance >= 200:
    print('O seu custo de viagem é de R$0,45 por km. Totalizando R$ {}'.format(viagem_longa))
else:
    print('O seu custo de viagem é de R$0,50 por km. Totalizando R$ {}'.format(viagem_curta) )
