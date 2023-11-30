# Crie um programa que simule o funcionamento de uma caixa eletrônico. No início, pergunte ao usuaráio qual será
# o valor desejado do saque (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Existem cédulas de 50, 20, 10 e 1 real


print('=-='*10)
print('{:^30}'.format('Banco Ferrari')) # :^30 quer dizer que minha frase tem 30 caracteres
# ou print(' '*7,'Banco Ferrari')
print('=-='*10)

valor = int(input("Informe o valor a ser sacado em R$: "))

nota50 = valor // 50
valor %=  50

nota20 = valor // 20
valor %= 20

nota10 = valor // 10
valor %= 10

nota1 = valor // 1

print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")

print('=-='*10)
print('Outra resolução')
print('=-='*10)

valor = int(input('Qual valor você quer sacar: R$ '))
cont_cinquenta = cont_vinte = cont_dez = cont_um = 0

while True:
    while valor - 50 >= 0:
        valor -= 50  #cada vez que ele diminui 50 ele faz uma contagem
        cont_cinquenta += 1
    while valor - 20 >= 0:
        valor -= 20 #cada vez que ele diminui 20 ele faz uma contagem
        cont_vinte += 1
    while valor - 10 >= 0:
        valor -= 10 #cada vez que ele diminui 10 ele faz uma contagem
        cont_dez += 1
    while valor - 1 >= 0:
        valor -= 1 #cada vez que ele diminui 1 ele faz uma contagem
        cont_um += 1
    break
if cont_cinquenta != 0:
    print(f'Total de {cont_cinquenta} cedulas de R$50')
if cont_vinte != 0:
    print(f'Total de {cont_vinte} cedulas de R$20')
if cont_dez != 0:
    print(f'Total de {cont_dez} cedulas de R$10')
if cont_um != 0:
    print(f'Total de {cont_um} cedulas de R$1')