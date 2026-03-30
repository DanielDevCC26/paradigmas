#prog aprimore o anterior mostrando no final a soma dos pares, a soma da terceira coluna, o maior da segunda linha.
#prog que cria uma matriz 3x3 com valores do teclado e mostra a matriz na tela
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos vlores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz [1][c]
    elif matriz [1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')