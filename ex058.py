#jogo em que o computador pensa vai "pensar" em um numero entre 0 e 10, o jogador tem que advinhar qual é o numero. Só que o jogador vai tentar até acertar. O programa deve dizer se o jogador venceu ou perdeu, e diz se acertou ou errou, e no final mostra quantas tentativas foram necessárias para vencer.
from random import randint
computador = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número entre 0 e 10. Será que você consegue adivinhar qual é?')
acertou = False   
palpites = 0
while not acertou:
  jogador = int(input('Qual é o seu palpite? '))
  palpites += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador < computador:
      print('Mais... Tente mais uma vez.')
    elif jogador > computador:
      print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))