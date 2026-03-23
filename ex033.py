#prog que leia tres numeros e que ostre qual é o maior e o menor
n1 = float(input('Digite um numero qualquer: '))
n2 = float(input('Digite outro numero qualquer: '))
n3 = float(input('Digite um terceiro numero qualquer: '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))