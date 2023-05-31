""" Aprimore o exercício anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matrix = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
even_sum = bigger = sum_column = 0

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))
        
print('-=' * 12)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end='')
        if matrix[row][column] % 2 == 0:
            even_sum += matrix[row][column]
    print()
print('-=' * 12)

print(f'A soma dos valores pare é {even_sum}')

for row in range(0, 3):
    sum_column += matrix[row][2]
print(f'A soma dos valores da terceira coluna é {sum_column}.')

for column in range(0, 3):
    if column == 0 or matrix[1][column] > bigger:
        bigger = matrix[1][column]
print(f'O maior valor da segunda linha é {bigger}')
