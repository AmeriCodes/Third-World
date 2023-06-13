"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em um lista. No final, mostre:

A) Quantas pessoas cadastradas 
B) A média de idade
C) Uma lista com mulheres.
D) uma lista com idade acima da média
"""
galera = list()
pessoas = dict()
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.').upper()[0]
    if continuar == 'N':
        break
print(galera)