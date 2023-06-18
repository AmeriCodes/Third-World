"""
Faça um programa que tenha um função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.
"""

from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    print(f'Contagem de {i} até {f} de {p} em {p}.')
   # sleep(2.5)
    print('-=' * 20)
    
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
           # sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
           # sleep(0.5)
            cont -= p
        print('FIM!')
        
# Main code
contador(1, 30, 7)
contador(10, 0, 2)
print('Agora, personalize sua contagem: ')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 20)

contador(inicio, fim, passo)
