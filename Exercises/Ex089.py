# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno indivdualmente.

ficha = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<18}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<18}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    pergunta_específica = int(input('Mostrar nostas de qual aluno? (999 interrompe): '))
    if pergunta_específica == 999:
        break
    if pergunta_específica <= len(ficha) - 1:
        print(f'Notas de {ficha[pergunta_específica][0]} são {ficha[pergunta_específica][1]}')
print('<<< VOLTE SEMPRE >>>')