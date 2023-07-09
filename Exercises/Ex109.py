"""
Modifique as funções que foram criadas no Ex107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no Ex108
"""

from practicus import numeri

entrada = float(input('Digite o preço: R$ '))

print(f'A metade de {numeri.real(entrada)} é {numeri.metade(entrada, True)}')
print(f'O dobro de {numeri.real(entrada)} é {numeri.metade(entrada, True)}')
print(f'Aumentando 10%, temos {numeri.aumentar(entrada, 10, True)}')
print(f'Reduzindo 20%, temos {numeri.diminuir(entrada, 20, True)}')