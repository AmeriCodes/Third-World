# Desenvolva um programa que leia quatro valores pelo teclado e guardi-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

number = (int(input('Digite um número')),
          int(input('Digite outro número')),
          int(input('Digite mais um número')),
          int(input('Digite o último número')))
print(f'Você digitou os valores {number}')
print(f'O valor 9 apareceu {number.count(9)} vezes.')
if 3 in number:
    print(f'O primeiro número 3 apareceu na posição {number.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in number:
    if n % 2 == 0:
        print(n, end=' ')
        