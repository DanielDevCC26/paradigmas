#um prog que mostre quantas vezes aparece a letra a, quando aparece primeiro e quando aparece por ultimo

nome = input('Digite seu nome completo: ').upper().strip()

print('A letra A aparece', nome.count('A'), 'vezes')
print('A primeira vez que aparece na posição', nome.find('A'))
print('A última vez que aparece na posição', nome.rfind('A'))