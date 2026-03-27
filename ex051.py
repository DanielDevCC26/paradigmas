#prog que faça um PA e mostre os 10 primeiros termos
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1)*razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end='-')