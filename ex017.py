#faça um programa que leia o comprimento do cateto oposto e do cateto adjecente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjascente? '))
hi = hypot (co, ca)
print('A hipotenusa é: {:.2f}'.format(hi))