# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Sorteei os valores: ', end='')

for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

#* Só depois de fazer o exercício eu percebi que era para fazer com tuplas, então deixei a resposta do professor a frente da minha, pôs de fato não conseguiria fazer
"""
from random import randint
bigger = smaller = 0
print("Os valores sorteados foram:",end=' ')
for c in range(0,5):
    number = randint(0,10)
    print(number, end=' ')
    if c == 0:
        bigger = number
        smaller = number 
    elif number > bigger:
        bigger = number
    elif number < smaller:
        smaller = number
print(f'\nO maior valor foi {bigger}')
print(f'O menor valor foi {smaller}')
"""