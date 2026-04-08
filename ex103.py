#prog com função ficha() que recebe dois param opc, nome do jogador e quantos gols fez. o prog deve mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')

n = str(input("Nome do Jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)