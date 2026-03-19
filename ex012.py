#algoritmo que le o preço de um produto e mostre um novo preço com 5% de desconto

p = float(input('Qual o preço do produto? '))
pd = p*0.95
print(f'O valor com desconto é de R${pd:.2f}')