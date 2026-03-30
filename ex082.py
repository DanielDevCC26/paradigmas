#prog que le numeros e coloca em lista, crie duas listas extras que vão conter os numeros pares e impares. ao final mostre os conteúdos das 3 listas.
lista = []
pares = lista[:]
impares = lista[:]

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')