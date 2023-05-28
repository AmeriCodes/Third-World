# Faça um programa que leia nome e peso de várias pessoas. guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


peaple = list()
data = list()
heavy = light = weight = 0
heavy_person = []
light_person = []
name = ' '

while True:
    try:
        while True:
            nome = input('Nome: ')
            if nome.isalpha():
                data.append(nome)
                break
            else:
                print("Entrada inválida. Por favor, digite apenas letras.")
        
        while True:
            weight = input('Peso: ')
            if weight.isnumeric():
                weight = float(weight)
                data.append(weight)
                break
            else:
                print("Entrada inválida. Por favor, digite apenas números.")

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
            elif data[1] == heavy and data[1] == light:
                heavy_person.append(data[0])
                light_person.append(data[0])
            elif data[1] == heavy:
                heavy_person.append(data[0])
            elif data[1] == light:
                light_person.append(data[0])
        data.clear()
        
        answer = " "
        answer = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if answer == 'n':
            break
        else:
            while answer != 's':
                answer = str(input('Digite "S" se deseja continuar e "N" se não. '))[0]
    except ValueError:
        print('Entrada errada, tente de novo')
        
print(f'{len(peaple)} pessoas foram cadastradas')
print(f'O maior peso foi {heavy}Kg. Peso de {heavy_person}')
print(f'O menor peso foi de {light}Kg. Peso de {light_person}')
