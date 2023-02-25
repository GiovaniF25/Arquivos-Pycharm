# Criando uma função resumo, para não precisar ficar colocando várias vezes o print

from MODULARIZAÇÃO.desafio_110 import moeda

p = float(input('Digite o preço: R$ '))
taxa_aumento = float(input('Digite a taxa de aumento (%):  '))
taxa_desconto = float(input('Digite a taxa de aumento (%):  '))
moeda.resumo(p, taxa_aumento, taxa_desconto)
