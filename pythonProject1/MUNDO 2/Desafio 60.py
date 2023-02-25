# Faça um programa que leia um número qualquer e mostre o seu fatorial:

import math

numero = int(input('Digite um número qualquer para calcular o seu fatorial:'))
fatorial = math.factorial(numero)
print('O fatorial do {} é {}'.format(numero, fatorial))

# USANDO O FOR FICA:

n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for c in range(n1, 0, -1):
    acumulador *= c
print('O produto de todos os números é {}'.format(acumulador))

# assim eu só vejo o número final, mas eu quero ver todas as muliplicações, então (USANDO O WHILE):

n = int(input('Digite um número inteiro qualquer para descobrir o seu fatorial: '))
print('Calulando {}!'.format(n))

contador = n #sempre antes do while eu preciso colocar isso antes, isso daqui vai dizer qual é a primeira coisa que vai aparecer no while (aqui contador = n pq o primeiro numero do contador vai ser o N
fatorial = 1 # aqui vai 1 pq o primeiro termo de uma multiplicação é sempre o 1

while contador > 0:
    print('{} '.format(contador), end = ' ')
    print('x' if contador > 1 else ' = ', end = ' ' )
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))





