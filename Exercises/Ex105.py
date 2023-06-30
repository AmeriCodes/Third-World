"""
Faça um programa que tenha uma função 'notas()' que pode receber várias notas de alunos e vai retornar um dicionário com as seguinte informações:

→ Quantidade de notas
→ A maior nota 
→ A menor nota
→ A média da turma
→ A situação (opcional)
Adicione também as docstrings.

"""
def notas(*n, sit=False):
    """
        Função para analisar notas e situações de vários alunos.
    :parametro n: uma ou mias notas dos alunos (aceita várias).
    :parametro sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    
    r = {}
    
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    
    if sit:
        if r['media'] >= 8:
            r['situacao'] = 'BOA'
        elif r['media'] >= 6:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
            
    return r



resp = notas(5.5 , 2.5, 1.5, sit= True)
print(resp)
help(notas)