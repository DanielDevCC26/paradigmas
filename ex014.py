#prog que informe a temperatura em graus celcius e converta para fairenheit

c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5)+32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))