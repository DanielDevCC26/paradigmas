#prog que lê a velcidade do carro. se ultrapassar 80km/h diz que foi multado, a multa é de 7 reais por km excedido

speed = int(input('Qual a vlocidade que o carro atingiu? '))

if speed > 80:
    print('Você ultrapassou o limite e será multado.')
    multa = (speed-80)*7
    print('Você ultrapassou o limite de velocidade. Sua multa será de R${:.2f}'.format(multa))
else:
 print('Tenha um bom dia e boa viagem!')