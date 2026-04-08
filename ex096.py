#prog que tenha uma def chamada area() que receba dimensões de um terreno retangular (largura e comprimentoe mostre a area do terreno.
def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é de {a}m2')


print('Controle de terrenos')
print()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)