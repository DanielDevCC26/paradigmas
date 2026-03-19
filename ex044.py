#prog valor a ser pago, se dinheiro 10% desconto, credito a vista 5%, em 2x mantém, 3x ou mais 20% a mais

valor = float(input('Qual o valor do produto? '))
fp = input('Forma de pagamento (dinheiro / cartao_avista / cartao_2x / cartao_3x): ').strip().lower()

if fp == 'dinheiro':
    total = valor - (valor * 0.10)
elif fp == 'cartao_avista':
    total = valor - (valor * 0.05)
elif fp == 'cartao_2x':
    total = valor
else:
    total = valor + (valor * 0.20)

print('O valor a ser pago é de {:.2f}'.format(total))