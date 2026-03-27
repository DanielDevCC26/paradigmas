#soma de todos os numeros impares que são multiplos de tres no intervalo de 1 a 500

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c

print('O resultado da soma dos {} é {}:'.format(cont, soma))