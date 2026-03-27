'''prog que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. o prog será interrompido 
quando o número solicitado for negativo.'''

while True:
    n = int(input('Que ver a tabuada de qual número?  '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')
    print('-' * 30)
print('Programa de tabuada encerrado!')