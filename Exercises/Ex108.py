"""
Adapte o código do exercício 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""


from practicus import numeri

entrada = float(input('Digite o preço: R$ '))

print(f'A metade de {numeri.real(entrada)} é {numeri.real(numeri.metade(entrada))}')
print(f'O dobro de {numeri.real(entrada)} é {numeri.real(numeri.dobro(entrada))}')
print(f'Aumentando 10%, temos {numeri.real(numeri.aumentar(entrada, 10))}')