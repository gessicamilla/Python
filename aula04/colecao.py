def soma(valores):
    """ A função realiza a soma dos valores que estão em uma lista. Retorna o resultado da soma """
    rs = 0
    for i in valores:
        rs += i
    return rs

def media(valores):
    """ A função media realiza a soma dos valores e divide pela quantidade de valores somados e retorna o resuktado """
    rs = 0
    qtd = len(valores)
    for i in valores:
        rs += i
    return rs/qtd

def maior(valores):
    """ A função maior retorna o maior valor de uma lista """
    m = valores[0]
    for i in valores:
        if i > m:
            m = i
    return m

def menor(valores):
    """ A função menor retorna o menor valor de uma lista """
    m = valores[0]
    for i in valores:
        if i < m:
            m = i
    return m