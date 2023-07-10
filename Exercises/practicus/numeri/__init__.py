def aumentar(preco=0, taxa=0, format=False):
    resposta = preco + (preco * taxa / 100)
    return resposta if format is False else real(resposta)


def diminuir(preco=0, taxa=0, format=False):
    resposta = preco - (preco * taxa / 100)
    return resposta if format is False else real(resposta)
    
    
def dobro(preco=0, format=False):
    resposta = preco * 2
    return resposta if not format else real(resposta)


def metade(preco=0, format=False):
    resposta = preco / 2
    return resposta if not format else real(resposta)


def real(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxa_aumento=20, taxa_diminui=20):
    print('-' * 34)
    print('RESUMO DO VALOR'.center(34))
    print('-' * 34)
    print(f'Preço analisado: \t{real(preco)}')
    print(f'Dobro do preço: \t{real(dobro(preco))}')
    print(f'Metade do preço: \t{real(metade(preco))}')
    print(f'Com {taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'Com {taxa_diminui}% de redução: \t{diminuir(preco, taxa_aumento, True)}')
    print('-' * 34)