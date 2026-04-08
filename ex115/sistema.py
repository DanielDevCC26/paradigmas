from ex_lib.interface import *
from ex_lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break

    else:
        print('ERRO: digite uma opção válida!')

    sleep(2)