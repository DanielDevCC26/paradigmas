num = int(input('Digite um valor: '))
fatorial = 1

contador = num

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'Fatorial de {num} é {fatorial}')