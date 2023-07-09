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

