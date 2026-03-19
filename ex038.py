#prog que leia dois numeros inteiros e compareos mostrando qual é o maior e o menor valor

v1 = int(input('Escreva um valor inteiro: '))

v2 = int(input('Escreva outro valor inteiro: '))

if v1 > v2:
  print('O primeiro valor é maior que o segundo')
elif v1 == v2:
  print('Os dois valores são iguais')
else:
  print('O segundo valor é maior que o primeiro')
