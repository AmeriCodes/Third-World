"""
Dentro do pacote, crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from practicus import numeri

valor = numeri.leia_real("Digite o preço: R$")
numeri.resumo(valor, 30, 10)

