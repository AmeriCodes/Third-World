# Faça um programa que leia nome e peso de várias pessoas. guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.




peaple = list()
data = list()
heavy = 0
light = 0
heavy_person = []
light_person = []

while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    peaple.append(data[:])
    
    if len(peaple) == 1:
        heavy = data[1] 
        heavy_person.append(data[0])
        light = data[1]
        light_person.append(data[0])
    else:
        if data[1] > heavy:
            heavy = data[1]
            heavy_person = [data[0]]
        elif data[1] < light:
            light = data[1]
            light_person = [data[0]]
    data.clear()
    
    answer = " "
    answer = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if answer == 'n':
        break
print(f'{len(peaple)} pessoas foram cadastradas')
print(f'O maior peso foi {heavy}Kg. Peso de {heavy_person}')
print(f'O menor peso foi de {light}Kg. Peso de {light_person}')
