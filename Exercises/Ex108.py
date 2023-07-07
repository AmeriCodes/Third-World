


from practicus import numeri

entrada = float(input('Digite o preço: R$ '))

print(f'A metade de {numeri.moeda(entrada)} é {numeri.moeda(numeri.metade(entrada))}')
print(f'O dobro de {numeri.moeda(entrada)} é {numeri.moeda(numeri.dobro(entrada))}')
print(f'Aumentando 10%, temos {numeri.moeda(numeri.aumentar(entrada, 10))}')