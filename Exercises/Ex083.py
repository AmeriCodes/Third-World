# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos fechados na ordem correta.

express = str(input('Digite a expressão: '))
pilha = []
for symbol in express:
    if symbol == '(':
        pilha.append('(')
    elif symbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
    