# Crie um programa que crie um matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for column in range(0, 3):
            matrix[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))
print('=-' * 30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()