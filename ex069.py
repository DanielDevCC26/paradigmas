#prog de cadastro com idade sexo

maior_idade = 0
male = 0
female = 0
while True:
    idade = int(input('Qual sua idade?  '))
    sexo = str(input('Qual seu sexo? [M/F]')).strip().upper()

    if sexo == 'M':
        male +=1
    elif sexo == 'F' and idade < 20:
        female += 1
    if idade > 18:
        maior_idade += 1
    
    mais_um = str(input('Deseja cadastrar mais alguém? [S/N]')).strip().upper()
    
    if mais_um == 'N':
        break
    
    print('Ok. Vamos continuar.')
print(f'Você cadastrou {maior_idade} pessoas com mais de 18 anos. {male} homens. {female} mulheres com menos de 20 anos')