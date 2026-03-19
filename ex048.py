#soma de todos os numeros impares que são multiplos de tres no intervalo de 1 a 500

soma = 0

for c in range(1, 501, 2):  # só ímpares
    if c % 3 == 0:
        soma += c

print('O resultado da soma é:', soma)