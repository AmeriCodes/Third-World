lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata')

for comida in lanche:
    print(f'Comi {comida}')

print('=' * 30)

for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]} na posição {cont}')

print('=' * 30)

for pos, comida in enumerate(lanche):
    print(f'Comi {comida} na posição {pos}')
print('Comi para caramba!')

print('=' * 20)

print(sorted(lanche)) # essa função "sorted", coloca em ordem, transformando em lista, por isso que na saída, o programa troca os parênteses por colchetes
print(lanche) # mas repare que de fato não altera a tupla, pois é imutável

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # quando 'somamos uma tupla' ela não soma de verdade, ela agrega, junta uma na outra, por isso faz diferança se 'c = b + a' ou 'c = a + b' pois a variável que fica logo após o símbolo de igual sairá antes da outra.
print(c)
print(len(c)) # aqui diz qual o tamanho dessa tupla.
print(c.count(5)) # aqui eu descubro quando vezes aparece o número 5 na minha tupla.
print(c.index(2)) # aqui me onde está a primeira posição que o 2 aparece.
print(c.index(5, 1)) # aqui eu procurei onde estava o primeiro 5, partindo da posição 1, ou seja se eu tirar o um do código a resposta seria posição 0 pois tem um 5 na posição 0, mas como eu especifiquei que quero que começe da posição 1 para frente, ele só achará o próximo 5 que está na posição 5
print('=' * 30)

pessoa = ('Gustavo', 39, 'M', 99.88) # Diferente de outras linguagens de onde os vetores só aceitam informações do mesmo tipo, no python as tuplas aceitam vários tipos juntos sem problema.
print(pessoa)
print('=' * 30)

# A tupla é imutável, mas eu consigo apagar ela usando o comando 'del(pessoa)', nesse caso especificamente.
pessoa2 = ('Américo', 23, 'M', 84)
del(pessoa2)
print(pessoa2)
