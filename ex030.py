#prog que analisa se um numero é par ou impar

num = int(input('me diga um num qualquer: '))
resultado = num % 2
if resultado == 0:
    print('o numero {} é par'.format(num))
else:
    print('o numero {} é impar'.format(num))