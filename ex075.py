'''prog que le quantro valores pelo teclado e guarda em uma tupla
no final mostra: a- quantas vezes apareceu 9, b- em que posição 
foi digitado o numero 3, c- quais foram pares'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')