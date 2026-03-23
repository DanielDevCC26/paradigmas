#prog que le dois valores e mostre um menu na tela

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    print('\n[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print(f'Soma: {valor1 + valor2}')

    elif opcao == 2:
        print(f'Multiplicação: {valor1 * valor2}')

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior é {valor1}')
        elif valor2 > valor1:
            print(f'O maior é {valor2}')
        else:
            print('Os dois são iguais')

    elif opcao == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Saindo do programa...')

    else:
        print('Opção inválida')