# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

full_list = list()
odd_numbers = list() # números ímpares
even_numbers = list() # números pares

while True:
    try:
        number = (int(input('Digite um número: ')))
        full_list.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

        question = ' '
        question = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        while question not in 'sn':
            question = str(input('Digite "S" para continuar e "N" para parar! [S/N] ')).strip().lower()[0]
        if question == 'n':
            break
    except ValueError:
        print('Entrada inválida. Este programa só lê números inteiros.')
print('=-' * 30)
print(f'A lista completa é {full_list}')
print(f'A lista de pares é {even_numbers}')
print(f'A lista de ímpares é {odd_numbers}')
