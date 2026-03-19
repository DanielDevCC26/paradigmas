#escreva o nome de uma cidade e diga se começa com santo

cidade = input('Digite o nome da cidade: ').strip()

print(cidade[:5].lower() == 'santo')