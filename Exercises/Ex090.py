# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo de estrutura na tela.

dictionary = {}
dictionary['name'] = str(input('Name: '))
dictionary['average'] = float(input('Average: '))
if dictionary['average'] >= 7:
    dictionary['status'] = 'Approved'
elif 5 <= dictionary['average'] < 7:
    dictionary['status'] = 'Last chance'
else:
    dictionary['status'] = 'Failed'
print()
for k, v in dictionary.items():
    print(f'{k} é igual a {v}')
