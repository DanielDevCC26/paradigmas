'''prog que gera uma tupla de 5 num aleatorios de 1 a 10, mostra 
os números gerados e mostra o maior e o menor'''

from random import randint

num = (randint(1, 10), 
       randint(1, 10), 
       randint(1, 10), 
       randint(1, 10), 
       randint(1, 10),)
print(f'Os valores gerados são: {num}')
print(f'O maior valor é: {max(num)}')
print(f'O menor valor é: {min(num)}')