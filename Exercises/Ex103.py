"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
"""
def player_stats(nome = 'desconhecido', gols = 0):
    print('-' * 30)
    nome_input = input('Player name: ')
    gols_input = input('Player gols: ')
    
    if nome_input:
        nome = nome_input
        
    if gols_input:
        gols = int(gols_input)
    
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


player_stats()
"""

# Resposta do professor abaixo


def ficha(jog='<desconhecido>', gol = 0):
    print(f'O jogador {n} marcou {g} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
    