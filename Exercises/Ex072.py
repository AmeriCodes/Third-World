# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até, vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    try:
        number = int(input('Digite um número entre 0 e 20: '))
        if number < 0 or number > 20:
            print('Número inválido. Tente novamente.')
        else:
            break
    except ValueError:
        print('Entrada inválida. Este programa só lê números.')
print(f'Você digitou o número {tupla[number]}')
