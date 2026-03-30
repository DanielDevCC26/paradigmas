#prog que cria uma matriz 3x3 com valores do teclado e mostra a matriz na tela
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()