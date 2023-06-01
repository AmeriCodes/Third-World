# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
data_games = list()
print('-' * 40)
print(f'{"JOGOS NA MEGA SENA":^40}')
print('-' * 40)
how_many = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, how_many):
    rand_number = list()
    
    while len(rand_number) != 6:
        number = randint(1, 60)
        if number not in rand_number:
            rand_number.append(number)
    rand_number.sort()
    data_games.append(rand_number[:])
    rand_number.clear()
    #print(f'Jogo {c+1}: {data_games[c]}')      <-- esse print já resolveria a questão, mas como eu queria usar o print abaixo, e não teria como pois cairia dentro do laço, fiz o enumerate como o professor fez.

print('-=' * 3, f'SORTEANDO {how_many} JOGOS', '-=' * 3)
for i, l in enumerate(data_games):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
