# CRIEI UMA FUNÇÃO NA PASTAS DADOS PARA FAZER UMA LEITURA COM NÚMEROS COM VIRGULAS E DAR UMA MENSAGEM
# CASO EU ESCREVA UM VALOR NÃO NÚMÉRICO

from MODULARIZAÇÃO.desafio_112.utilidadescev import moeda, dados

p = dados.leiaDinheiro('Digite o preço: R$ ')
taxa_aumento = float(input('Digite a taxa de aumento (%):  '))
taxa_desconto = float(input('Digite a taxa de aumento (%):  '))
moeda.resumo(p, taxa_aumento, taxa_desconto)


