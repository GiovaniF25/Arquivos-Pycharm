# Faça um programa que tenha uma função chamada contado que receba três parametos
# início, fim e passo e a realize a contagem
# Seu programa tem que realizar 3 ontagems atras da funcão criada
# a) de 1 até 10 de 1 em 1
# b) de 10 até 0 de 2 em 2
# c) Uma contagem personalizada

from time import sleep

print('-=-'*10)
print('Contagem de 1 até 10 de 1 em 1')
print('-=-'*10)
for c in range(0,11):
    sleep(0.3)
    print(c, end = ' ')

print('')
print('-=-'*10)
print('Contagem de 10 até 0 de 2 em 2')
print('-=-'*10)
for cc in range(-10,0,2):
    sleep(0.3)
    print(cc*-1, end = ' ')
print('')
# Contagem personalizada
print('-=-'*10)
print('Agora é a sua vez de começar uma contagem')

def contador(i,f,p):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    for ccc in range(inicio, fim+1, passo):
        sleep(0.3)
        print(ccc, end = ' ')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
