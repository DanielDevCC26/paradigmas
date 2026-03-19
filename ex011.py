# ler altura e largura de uma parede em metros, calcula a area e a quantidade  de tinta necessária para pintar, sabendo que cada litro pinta 2 m2
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura*largura
print(f'A área da parede é de: {area:.2f},m²')
print(f'Você precisará de: {area/2:.2f}l de tinta')