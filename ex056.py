'''prog que le o nome a idade e sexo de 4 pessoas. média de idade do grupo, 
nome do homem mais velho, quantas mulheres tem menos de 20 anos'''

from datetime import date

ano_atual = date.today().year

soma_idade = 0
nome_homem_mais_velho = ''
maior_idade_homem = 0
mulheres_menos_20 = 0

for c in range(1, 5):
    print(f'----Pessoa {c}: ')
    nome = input('Nome: ')
    idade = int(input('Ano que nasceu: '))
    sexo = input('Sexo: [M/F]').upper()

    idade = ano_atual - idade
    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media = soma_idade / 4

print(f'{nome_homem_mais_velho} é o homem mais velho.')
print(f'{mulheres_menos_20} mulheres tem menos de 20 anos.')
print(f'A média de idade do grupo é de {media:.1f}anos.')