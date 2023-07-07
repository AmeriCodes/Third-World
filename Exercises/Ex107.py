"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from practicus import numeri

entrada = float(input('Digite o preço: R$ '))
print(f'A metade de {entrada} é {numeri.metade(entrada)}')
print(f'O dobro de {entrada} é {numeri.dobro(entrada)}')
print(f'Aumentando 10%, temos R${numeri.aumentar(entrada, 10)}')