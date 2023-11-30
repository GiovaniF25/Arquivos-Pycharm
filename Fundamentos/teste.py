def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1

valores = [3,6,9,12]
dobra(valores)
print(valores)