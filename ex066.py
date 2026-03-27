'''prog que que le varios numeros inteiros pelo teclado. 
o prog só vai parar quando digitar o valor 999, que é a 
condição de parada. no final, mostre quantos números foram 
digitados e qual foi a soma entre eles, desconsiderando o flag.'''

soma = n = cont = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números. A soma dos valores é de {soma}')