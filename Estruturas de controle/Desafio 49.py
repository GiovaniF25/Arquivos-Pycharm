# Refaça o exercício 09 e crie um programa que mostre a taboada do numero escolhido:

numero = int(input('Digite um número para saber a sua taboada:'))
print('A taboada do {} é:'.format(numero))

for c in range(1,11):
    print('{}*{}={}'.format(numero, c, numero*c))
