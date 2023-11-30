# Crie um programa que gere 5 número aleatórios e coloque em uma TUPLA. Depois disso, mostre uma lista
# dos números gerados e indique o maior e o menor valor que estão na TUPLA

from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

tupla = (n1, n2, n3, n4, n5)
# ou fazer n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('Sorteio:')
for c in tupla:
    print(c, end=' ')

print('')
print(f' O maior número sorteado foi: {max(tupla)}')
print(f' O menor número sorteado foi: {min(tupla)}')