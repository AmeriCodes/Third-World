# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em um lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    try:
        while True:
            number = int(input('Digite um valor: '))
            if number not in lista:
                print('Valor adicionado com sucesso...')
                lista.append(number)
                break
            else:
                print('Valor duplicado! Não será adicionado.')
        
        pergunta = ' '
        while pergunta not in 'SN':
            pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if pergunta == 'N':
            break
    except ValueError:
        print('Entrada inválida. Este programa só lê números inteiros.')
print('-=' * 25)
lista.sort()
print(lista)