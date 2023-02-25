#MODULARIZAÇÃO

def fatorial(x):
    """
    :param x: número que desejo fazer o fatorial
    :return: faz o calculo do fatorial
    """
    p = 1
    for c in range(x,0,-1):
        p =p*c
    return p

def dobro(x):
    resposta = x*2
    return resposta
