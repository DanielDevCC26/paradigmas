#prog que digita 7 valores diferentes e cadastra em uma unica lista, que separe pares de impares. no final mostra os valores em ordem crescente
num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores: {num}')