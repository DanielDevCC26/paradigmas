#prog que le numeros inteiros e mostra se o numero 5 está na lista
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}: ')
if 5 in valores:
    print('5 está na lista.')
else:
    print('5 não está a lista.')