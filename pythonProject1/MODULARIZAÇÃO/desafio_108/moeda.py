
def aumentar(preço = 0, taxa = 0):
    resultado = preço + (preço*taxa/100)
    return resultado


def diminuir(preço = 0, taxa = 0):
    resultado = preço - (preço*taxa/100)
    return resultado


def dobro(preço = 0):
    resultado = preço * 2
    return resultado


def metade(preço = 0):
    resultado = preço / 2
    return resultado

def leitura(preço = 0, moeda = 'R$'):
    resultado = f'{moeda}{preço:.2f}'.replace('.',',')  #aqui eu automatizei o R$, troquei o . por , e coloquei 2 casas decimais depois da virgula
    return resultado
