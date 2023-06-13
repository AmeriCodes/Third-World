"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em um lista. No final, mostre:

A) Quantas pessoas cadastradas 
B) A média de idade
C) Uma lista com mulheres.
D) uma lista com idade acima da média
"""
galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.').upper()[0]
    if continuar == 'N':
        break
print(f'{"ANALISE DE DADOS":-^40}')
print(f'A) - {len(galera)} pessoas foram cadastradas')
media = soma / len(galera)
print(f'B) - A media de idade é de {media:5.2f} anos.')
print('C) - As mulheres cadastradas foram, ' , end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('D) - Lista das pessoas acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(f'{"Encerrado":-^40}')
