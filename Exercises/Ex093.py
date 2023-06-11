"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
"""

dicionario = dict()
gols_por_partida = list()
total_de_gols = 0

dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f"Quantas partidas {dicionario['nome']} jogou? "))
for gols in range(partidas):
    gols_por_partida.append(int(input(f'Quantos gols na partida {gols + 1}: ')))
    total_de_gols += gols_por_partida[gols]

dicionario['gols'] = gols_por_partida[:]
dicionario['total'] = total_de_gols

print('=-=' * 25)
print(dicionario)
print('=-=' * 25)

for v, k in dicionario.items():
    print(f'O campo {v} tem o valor {k}.')
print('=-=' * 25)

print(f'{dicionario["nome"]} jogou {partidas} partidas.')
for i in range(0, partidas):
    print(f'=> Na partida {i + 1}, fez {gols_por_partida[0 + i]}')
print(f'Foi um total de {total_de_gols} gols.')

# O algorítimo abaixo foi a resposta do professor.

"""
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
"""