"""
Reescreva a função leiaInt() que fizemos no ex 104, incluindo agora apossibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print(f'ERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return n
        
        
def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print(f'ERRO: por favor, digite um número real válido.')
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return n
        
        
n1 = leia_int('Digite um número inteiro: ')
n2 = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')