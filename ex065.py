#prog que le numero inteiros, mostra quantos numeros foram digitados, o menor valor e a media e pergunta quando quer parar

resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número:  '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant}, a média foi {media}, o menor foi {menor} e o maior foi {maior}.')