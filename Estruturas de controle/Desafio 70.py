# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
# o usuario vai continuar. No final, mostre:
# -O total gasto
# -Quantos produtos custam mais de R$ 1.000
# -Qual é o nome do produto mais barato

print('=-='*10)
print('        lOJAS FERRARI')
print('=-='*10)

soma = 0
lista_nome = []
lista_preco = []

while True:
    nome = str(input('Digite o nome do produto: ')).upper()
    lista_nome.append(nome)
    preco = float(input('Digite o preço do produto em R$: '))
    lista_preco.append(preco)

    contador = 0
    if preco > 1000:
        contador += 1

    continuar = str(input('Quer comprar mais algum produto? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite novamente. Quer comprar mais algum produto? [S/N]: ')).strip().upper()[0]
    soma += preco

    if continuar not in 'S':
        break

print(' ')
print(f'Foi gasto um total de R$ {soma:.2f} ')
print(f'Existem {contador} produtos que custam mais de R$ 1.000 ')
print('O produto mais barato comprado foi o item {}'.format(lista_nome[lista_preco.index(min(lista_preco))]))
print('O preço do produto mais barato comprado foi R$ {:.2f}'.format(min(lista_preco)))

print(' ')
print('Compra finalizada')
