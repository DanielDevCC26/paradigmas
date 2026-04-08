#prog qu tenha uma lista chamada numeros, e duas defs chamadas sorteio e somapar. a primeira sorteia 5 numeros e coloca na lista, a segunda vai mostrar a soma dos num pares.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 numeros da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)