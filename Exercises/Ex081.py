# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    value = int(input('Digite um número: '))
    lista.append(value)

    question = ''
    question = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while question not in 'ns':
        question = str(input('Digite "S" para continuar e "N" para parar! [S/N] ')).strip().lower()[0]
    if question == 'n':
        break

lista.sort(reverse=True)        
number5 = 5 in lista # Ideia do GPT
print('=-' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
print(f'O número 5 {"está presente" if number5 else "não está presente"} na lista.') # Tinha uma maneira de fazer essa parte na mente, mas busquei outras e achei esse interessante, quis registrar.
