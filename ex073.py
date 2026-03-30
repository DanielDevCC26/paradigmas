'''crie uma tupla preenchida com os 20 primeiros 
colocados da tabela do campeonato brasileiro de futebol, na ordem
de colocação. depois mostre a-apenas os 5 primeiros colocados, 
b-os ultimos 4 colocados, c-uma lista com os times em ordem
alfabética, d- em que posição na tabela está o time chapecoense.'''

tabela = (
    'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Athletico Paranaense', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
    'Vasco da Gama', 'América Mineiro', 'Sport Recife', 'Vitória', 'Paraná'
)

print(f'Estes são os cinco primeiros colocados do Brasileirão: {tabela[0:5]}')
print(f'Os últimos 4 colocados: {tabela[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print(f'A chapecoense terminou o campeonato em {tabela.index('Chapecoense')}')