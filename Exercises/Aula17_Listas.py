# Teoria da primeira parte da aula de listas
#*DIFERENTE DAS TUPLAS, LISTAS SÃO MUTÁVEIS

lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim'] # Em vez de usar parênteses, usamos colchetes nas listas.
print(lanche[2])

lanche[3] = 'Picolé' # Nesse comando eu consigo alterar o trocar o 'Pudim' pelo 'Picolé'.
lanche.append('Biscoito') # Este comando adiciona itens no final da minha lista.
lanche.insert(0, 'Cachorro-quente') # Com esse método eu adiciono na posição específica.
del lanche[3] # Esse comando serve para deletar um item
lanche.pop(3) # Esse comando normalmente é usado para deletar o último item da lista, mas se for especificado o item, ele também apaga.
if 'Pizza' in lanche:
    lanche.remove('Pizza') # Esse método também apaga, porem em vez de apagar por índice, apaga por conteúdo. #* Ele só apaga a primeira ocorrência do conteúdo, caso tenha mais de uma.
lista= list(range(4,11)) # Aqui eu crio listas atravéz de 'range'.

valores = [8, 2, 5 , 4, 9, 3, 0]
valores.sort() # Aqui ele ordena os valores, no caso deixaria '0, 2, 3, 4, 5, 8, 9'
valores.sort(reverse=True) # Esse comando ordenaria de forma invertida, '9, 8, 5, 4, 3, 2, 0'

test = list()
for cont in range(0,5):
    test.append(int(input('Digite um valor: ')))

for c, v in enumerate(test):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# No Pyhton, quando criamos igualamos uma lista na outra nós criamos um vínculo entre elas, e qualquer alteração feita em uma será feita na outra.
a = [2, 3, 4, 7]
b = a # Como aqui
# Se quisermos que uma lista receba outra mas as alterações sejam feitas individualmente, então termos que fazer que com que a uma lista receba os 'ítens' de outra, e não a lista, por meio desse código abaixo.
b = a[:] # Fazendo assim as alterações em 'b' só alteraram 'b'.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
