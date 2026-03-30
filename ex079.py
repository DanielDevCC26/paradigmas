#prog onde usuario pode digitar varios valores numericos e cadastrar em uma lista. caso o numero ja exista la dentro, ele não será adicionado. no final serão exibidos todos os valores digitados em prdem crescente.

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar.')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')