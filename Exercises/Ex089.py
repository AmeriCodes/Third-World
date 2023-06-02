# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno indivdualmente.

report_card = list()
while True:
    name = str(input('Nome: ')).strip().title()
    grade1 = float(input('Nota 1: '))
    grade2 = float(input('Nota 2: '))
    average = (grade1 + grade2) / 2
    report_card.append([name, [grade1, grade2], average])
    question = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if question == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<18}{"MÉDIA":>8}')
print('-' * 26)
for i, studant in enumerate(report_card):
    print(f'{i:<4}{studant[0]:<18}{studant[2]:>8.1f}')
while True:
    print('-' * 30)
    specific_question = int(input('Mostrar nostas de qual aluno? (999 interrompe): '))
    if specific_question == 999:
        break
    if specific_question <= len(report_card) - 1:
        print(f'Notas de {report_card[specific_question][0]} são {report_card[specific_question][1]}')
print('<<< VOLTE SEMPRE >>>')