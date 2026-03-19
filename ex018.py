# faça um prog que leia um angulo qq e mostre na tela o valor do seno cosseno e tangente desse angulo

from math import sin, cos, radians

a = float(input('Qual o valor do angulo? '))
s = sin(radians(a))
c = cos(radians(a))
print(f'O seno deste angulo é: {s:.2f}')
print(f'O cosseno deste angulo é: {c:.2f}')
