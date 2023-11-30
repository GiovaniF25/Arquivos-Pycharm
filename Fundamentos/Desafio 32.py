# Faça um programa que leia um ano e mostre se ele é bissexto

ano= int(input('Digite um ano: '))
verificacao= ano % 4

if verificacao == 0  :
    print('O ano escolhido é um ano bissexto!')
else:
    print('O ano escolhido não é um ano bissexto!')