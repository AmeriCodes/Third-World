# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
bigger = minor = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        bigger = minor = lista[c]
    else:
        if lista[c] > bigger:
            bigger = lista[c]
        if lista[c] < minor:
            minor = lista[c]
print('#=' * 20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {bigger} nas posições ', end='')
for i, v in enumerate(lista):
    if v == bigger:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {minor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == minor:
        print(f'{i}...', end='')