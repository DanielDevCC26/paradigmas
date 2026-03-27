print('GERADOR DE PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos? (0 para parar): '))

print('Fim! Total de termos mostrados:', total)