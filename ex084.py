#prog que le nome e peso de pessoas, em uma lista, mostrando mais pesados e mais leves
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]:'))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso é de {maior} quilos. Peso de', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f' O menor peso é de {menor} quios. Peso de', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()