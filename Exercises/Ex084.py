# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


peaple = list() # lista final
data = list() # sub lista
heavy = light = weight = 0 # onde seram armazenados os pesos
heavy_person = []
light_person = []

while True:
    try: # O try e o except são são utilizados aqui caso haja algum erro de conversão do weight para float já que a validação do name e do weight estão sendo feitas pelo laço while True:.
        while True:
            name = input('Nome: ')
            if name.isalpha(): # Função que garante que o digitado será apenas letras.
                data.append(name)
                break
            else:
                print("Entrada inválida. Por favor, digite apenas letras.")
        
        while True:
            weight = input('Peso: ')
            if weight.isnumeric(): # Função que garante que o digitado será apenas números.
                weight = float(weight) # Conversão para float por estética.
                data.append(weight)
                break
            else:
                print("Entrada inválida. Por favor, digite apenas números.")

        peaple.append(data[:]) # Cópia da sub lista para a final
        
        if len(peaple) == 1: # Como esse len está depois do append ele será validado.
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
            elif data[1] == heavy and data[1] == light: # Caso fosse digitado várias pessoas com o mesmo peso o programa deveria entender e colocar todas elas nas listas de mais pesadas e mais leves, mas ele não estava acontecendo, então esse 'elif' foi adicionado depois para tentar remediar esse erro.
                heavy_person.append(data[0])
                light_person.append(data[0])
            elif data[1] == heavy:
                heavy_person.append(data[0])
            elif data[1] == light:
                light_person.append(data[0])
        data.clear() # limpeza da sub-lista
        
        answer = " "
        answer = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
        if answer == 'n':
            break
        else:
            while answer != 's': # Validação de erro.
                answer = str(input('Digite "S" se deseja continuar e "N" se não. '))[0]
    except ValueError:
        print('Entrada errada, tente de novo')
        
print(f'{len(peaple)} pessoas foram cadastradas')
print(f'O maior peso foi {heavy}Kg. Peso de {heavy_person}')
print(f'O menor peso foi de {light}Kg. Peso de {light_person}')
