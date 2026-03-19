# crie um prog que leia o nome completo, com todas as letras maiusculas, com todas minusculas, quantas letras sem considerar espaços, quantas letras no primeiro nome

nome = input('Insira seu nome completo: ')
print('Nome em maiúsculas', nome.upper())
print('Nome em minúsculas', nome.lower())
print('Total de letras sem espaço', len(nome.replace(' ', '')))
primeiro_nome = nome.split()[0]
print('Letras no primeiro nome: ', len(primeiro_nome))