#prog que le 6 num int e mostre a soma dos pares
soma = 0

for i in range(6):
    num = int(input('Digite um número inteiro: '))
    
    if num % 2 == 0:
        soma += num

print('A soma dos números pares é:', soma)