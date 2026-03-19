#um prog que diz se a pessoa tem silva no nome

nome = input('Insira seu nome: ').strip()
print(nome[:5].lower() == 'silva')