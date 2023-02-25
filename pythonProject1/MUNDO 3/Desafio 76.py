# Crie uma programa que tenha uma tupla única com nomes de produtos e seus preços
# No final mostre uma lista de preçps, organizados de forma tabular

print('=-='*10)
print('{:^30}'.format('Listagem de preço'))
print('=-='*10)

listagem =  ('Lápis', 1.75,
             'Borracha', 2.00,
             'Caderno', 15.90,
             'livro', 34.90)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>5}')



