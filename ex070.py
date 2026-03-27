#prog que le o nome e o preço de um produto, deve perguntar se quer cadastrar mais produtos. No final mostra o valor total da compra, quantos produtos custam mais de mil e qual o produto mais barato.
tot = mais_de_mil = mais_barato = 0
barato = ' '

while True:
    prod = str(input('Produto: '))
    price = float(input('Preço: '))

    tot += price

    if price >= 1000:
        mais_de_mil += 1

    if mais_barato == 0:
        mais_barato = price
    elif price < mais_barato:
        mais_barato = price
        barato = prod

    ans = str(input('Gostaria de cadastrar mais um produto? [S/N]')).strip().upper()[0]
    if ans == 'N':
        break
print(f'Fim do registro!. O total da compra é de {tot}.')
print(f'{mais_de_mil} produtos custam mais de mil reais.')
print(f'O produto mais barato custou {mais_barato}')