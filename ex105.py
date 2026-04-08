#prog com função notas() que coloca notas de alunos em um dict e mostra quantidade de notas, maior nota, menor, média da turma, situação e docstrings

def notas(*n, sit=False):
    
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'RUIM'

    return r

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)