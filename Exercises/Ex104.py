"""
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico 
Ex:
n = leiaint('Digite um número: ')
"""
"""
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor


# Programa principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
"""

def leia_int():
    while True:
        try:
            valor = int(input('Digite um valor numérico inteiro: '))
            return valor
        except ValueError:
            print('Valor inválido. Tente novamente.')
            

numero = leia_int()
print('O número digitado foi: ',numero)