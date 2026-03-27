#prog que simula funcionamento de um caixa eletronico, no inicio pergunta o valor a ser sacado int, e o programa informa quantas cédulas serão entregues, somente cédulas de 50, 20, 10 e 1 real.

print('=' *30)
print('{:^30}'.format('Banco CEV'))
print('=' *30)
valor = int(input('Que valor você quer sacar: R$'))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break