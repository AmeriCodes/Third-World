# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[],[]]

for i in range(1,8):
    value = int(input(f'Digite o {i}o. valor: '))
    if value % 2 == 0:
        numbers[1].append(value)
    else:
        numbers[0].append(value)
print('-=' * 30)
numbers[1].sort()
numbers[0].sort()
print(f'Os valores pares digitados foram: {numbers[1]}')
print(f'Os valores ímpares digitados foram: {numbers[0]}')

