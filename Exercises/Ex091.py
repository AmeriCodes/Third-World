"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado.')

print(f'{"RANKING":-^25}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
