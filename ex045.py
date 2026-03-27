#prog jogo de jokenpo

from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint (0, 2)
print('''Suas opções:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador veceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada inválida')
