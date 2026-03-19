#um prog que mostre o nome, primeiro nome sozinho e ultimo nome sozinho

nome = input('Digite seu nome completo: ').strip()

partes = nome.split()

print('Primeiro nome:', partes[0])
print('Último nome:', partes[-1])