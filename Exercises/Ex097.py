"""
Faça um programa que tenha uma função que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')

saída
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
"""



def mensagem_variavel(msg):
    tamanho_da_mensagem = len(msg) +4
    print(f'{"=" * tamanho_da_mensagem}')
    print(f'  {msg}')
    print(f'{"=" * tamanho_da_mensagem}')


mensagem_variavel('testando')
mensagem_variavel('Américo')
mensagem_variavel("I'm learning English!")