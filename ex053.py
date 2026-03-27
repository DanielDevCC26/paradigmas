#prog que escreve um texto ao contrário e diz se é palindromo
frase = str(input('Escreva o texto: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]    
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')
