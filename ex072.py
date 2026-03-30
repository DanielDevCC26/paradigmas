'''programa que cria uma tupla totalmente preenchida com uma 
contagem por extenso de 0 a 20. seu programa deverá ler um 
número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

num = ('', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num_ext = int(input('Digite um número inteiro de 1 a 20: '))

print(f'Você digitou o número {num[num_ext]}')