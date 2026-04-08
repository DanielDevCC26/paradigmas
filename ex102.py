#prog com função fatorial() que recebe dois parametros. o primeiro indica um numero a calcular e o outro chamado show. que será um valor lógico indicando se será mostrado ou não na tela o processo de calculo do fatorial.
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))