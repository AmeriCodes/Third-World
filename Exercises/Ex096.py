"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def logo(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)
    


def area(largura, comprimento):
    answer = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {answer}m².')


logo('Controle de Terrenos')

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)

logo('Fim do Programa')
