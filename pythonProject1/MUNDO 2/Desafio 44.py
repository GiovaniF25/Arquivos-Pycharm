# Elaboar um programa que calculo o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# a vista dinheiro e cheque 10% de desconto
# a vista no cartão 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão 20% de juros


print('{:=^40}'.format(' Lojas Ferrari '))
print('{:^40}'.format('\033[1;31m Bem vindos!\033[m '))

preco_produto = float(input('Informe o preço do produto escolhido: '))
print('Opções de pagamento: \n Escolha entre: \n Opção 1: A vista no dinheiro ou cheque \n Opção 2: A vista no cartão \n Opção 3: 2x no cartão \n Opção 4: 3x ou mais no cartão ')


forma_pagamento = float (input('Escolha  entre as opções de pagamento 1, 2, 3 ou 4 '))

if forma_pagamento == 1:
    print('O valor do produto fica no valor de R$ {:.2f}, devidos aos 10% de desconto'. format(preco_produto*0.90))
elif forma_pagamento == 2:
    print('O valor do produto fica no valor de R$ {:.2f}, devidos aos 5% de desconto'.format(preco_produto * 0.95))
elif forma_pagamento == 3:
    print('O valor do produto fica no valor de R$ {:.2f}, sem nenhum desconto'.format(preco_produto))
elif forma_pagamento == 4:
    print('O valor do produto fica no valor de R$ {:.2f}, devidos aos 20% de juros'.format(preco_produto * 1.20))








