# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time Bahia.


leaderboard = ('Botafogo', 'Palmeiras','Cruzeiro', 'Fortaleza','São Paulo', 'Fluminense','Grêmio', 'Internacional','Bahia', 'Athletico-PR','Vasco', 'Bragantino','Cuiabá', 'Santos','Corinthians', 'Atlético-MG','Flamengo', 'Goiás','Coritiba', 'América-MG')

print('Os 5 primeiros colocados são:')
print('==' * 20)

for pos, team in enumerate(leaderboard):
    if pos >= 5:
        break
    print(f'{pos+1}º {team}')

print('==' * 20)
print('Os 4 últimos colocados são:')
print('==' * 20)

for cont in range(16, len(leaderboard)):
    print(f'{cont+1}º {leaderboard[cont]}')

          
print('==' * 20)
print('Lista dos times em ordem alfabética')
print('==' * 20)

ordem_alfabetica = sorted(leaderboard)
for item in ordem_alfabetica:
    print(item)

print('==' * 20)
print()