#prog que ajude a jogar na mega sena e criar palpites. o programa vai perguntar quantos jogos gerar e vai sortear 6 numeros entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta
from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(f'Os numeros sorteados foram {jogos}.')
