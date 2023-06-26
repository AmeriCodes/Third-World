"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        → Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostra ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    
    result = 1
    for i in range(1, n + 1):
        if show:
            print(i, end='')
            if i != n:
                print(' x ', end='')
            else:
                print(' = ', end='')
        result *= i
    return result    
    
    
    
print(fatorial(5, True))


# Resposta do professor abaixo:


def fatorial2(n, show=False):
    """
    fatorial(n, show=False)
        → Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostra ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial2(5, True))
            