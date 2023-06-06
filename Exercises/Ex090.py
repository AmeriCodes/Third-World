# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo de estrutura na tela.

d = {}
d['name'] = str(input('Name: '))
d['average'] = float(input('Average: '))
if d['average'] >= 7:
    d['status'] = 'Approved'
else:
    d['status'] = 'Failed'
for k, v in d.items():
    print(f'{k} = {v}')
