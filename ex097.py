#prof com def escreva() que recebe txt com qualquer parametro e mostre mensagem com tamanho adaptável
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('Daniel')