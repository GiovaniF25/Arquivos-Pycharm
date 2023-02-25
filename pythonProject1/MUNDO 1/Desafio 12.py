# Faça um algoritmo que leia o preço de um produto e mostre-o com 15% de desconto

preco = int(input('Qual é o preço do produto? '))
desconto = preco*0.85

print('O valor do produto considerando um desconto de 15% é de R$ {:.2f}'. format(desconto))