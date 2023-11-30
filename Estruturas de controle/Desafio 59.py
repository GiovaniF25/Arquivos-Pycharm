# Crie um programa que leia dois valores e mostre um MENU como a tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('''  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')

opcao = ''     # isso nao tem importancia, é só pra apresentar alguma coisa antes de colocar no while

while opcao != 5:
    opcao = int(input('Escolha uma das 5 opções: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1,n2,soma))
        print('=-='*10)

    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, multiplicacao))
        print('=-=' * 10)

    elif opcao == 3:
        if n1 > n2:
            print(' {} é maior que {}'.format(n1, n2))
            print('=-=' * 10)

        elif n2 > n1:
            print(' {} é maior que {}'.format(n2, n1))
            print('=-=' * 10)

    elif opcao == 4:
        novo_n1 = int(input('Digite novamente o n1: '))
        novo_n2 = int(input('Digite novamente o n2: '))
        print('=-=' * 10)

if opcao == 5:
    print('Fim do programa')