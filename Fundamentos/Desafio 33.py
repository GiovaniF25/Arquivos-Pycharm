# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
n = [n1, n2, n3]

print('O maior valor digitado foi {}'.format(max(n)))
print('O menor numero digitado foi {}'.format(min(n)))

#OU
n1 = int(input('digite o primeiro número:  '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input ('Digite o terceiro número: '))

lista = [n1, n2, n3]
lista_ordenada = sorted(lista)
print(lista_ordenada)
print('O menor número é {}'.format(lista_ordenada[0]))
print('O maior número é {}'.format(lista_ordenada[2]))