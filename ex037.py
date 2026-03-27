#prog que leia um numero inteio qq e peça para o usuario escolher qual será a base de conversão, 1 binário, 2 octal ou 3 hexadecimal
valor = int(input('Qual valor vc quer converter? '))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(valor, bin(valor)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(valor, oct(valor)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção inválida. Tente novamente!')