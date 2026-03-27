#prog par ou ímpar, será interrompido quando o jogador perder

from random import randint

while True:
    jogador = int(input('Digite um valor:  '))
    computador = randint(0,11)
    total = computador + jogador
    tipo = ' '
    v = 0
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. A soma foi de {total}')
    if tipo == 'P':
        if jogador % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            break
    elif tipo == 'I':
        if jogador % 2 == 1:
            print('Você venceu!')
            v += 1
    print('Vamos jogar novamente!')
print(f'Você perdeu. Mas conseguiu me vencer {v} vezes.')
            