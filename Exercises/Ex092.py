"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
dados = dict()
from datetime import datetime

dados['nome'] = input('Nome: ').title()
nascimento = input('Ano de nascimento: ')
dados['idade'] = datetime.now().year - int(nascimento[:4])
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = input('Salário: ')
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print(f'{"DADOS":=^36}')
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
    