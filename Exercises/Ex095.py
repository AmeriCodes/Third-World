"""
Aprimore o exercício 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total_de_partidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input('Quer cadastar mais jogadores? [S/N] ')).upper()[0]
        if resposta in "SN":
            break
        print('ERRO! Responda apenas S ou N. ')
    if resposta == 'N':
        break

print('-=' * 20)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
  
    for d in v.values():
        print(f'{str(d):<15}', end='')    
    print()

print('-=' * 20)

while True:
    busca = int(input('Mostrar dados de qual jogador? [PARAR > 999] '))
  
    if busca == 999:
        break
  
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
  
    else:
        print(f'{time[busca]["nome"]:-^40}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i + 1} fez {g} gols')
    print('-=' * 20)

print(f"{'VOLTE SEMPRE':-^40}")    
