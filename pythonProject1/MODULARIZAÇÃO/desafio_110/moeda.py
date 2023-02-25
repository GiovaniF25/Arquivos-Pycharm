def aumentar(preço = 0, taxa = 0, formato = False):
    '''
    # criei uma condição para escrever de uma forma formatada
    # eu escrevi True no teste_109, se eu escrevesse False ou deixasse sem nada (ele entende como False)
    # ele deixaria sem a formatação de leitura, como eu escrevi True, ele fez o resultado formatado para função leitura
    '''
    resultado = preço + (preço*taxa/100)
    return resultado if not formato else leitura(resultado)

def diminuir(preço = 0, taxa = 0, formato = False):
    resultado = preço - (preço*taxa/100)
    return resultado if not formato else leitura(resultado)

def dobro(preço = 0, formato = False):
    resultado = preço * 2
    return resultado if not formato else leitura(resultado)

def metade(preço = 0, formato = False):
    resultado = preço / 2
    return resultado if not formato else leitura(resultado)

def leitura(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')  #aqui eu automatizei o R$, troquei o . por , e coloquei 2 casas decimais depois da virgula

def resumo (preço = 0, taxaa = 0, taxad = 0 ):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{leitura(preço)}')
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de {taxaa}%: \t{aumentar(preço, taxaa, True)}')
    print(f'Aumento de {taxad}%: \t{diminuir(preço, taxad, True)}')
    print('-' * 30)

