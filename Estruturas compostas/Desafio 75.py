# Desenvola um programa que leia quatro valores pelo teclado e guarde-os em uma tuplas
# No final mostre:
# -Quantas vezes apareceu o número 9
# -Em que posição foi digitado o primeiro valor 3
# -Quais foram os números pares digitados

print('Digite 4 números aleatórios:')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))

tupla = (n1, n2, n3, n4)

print('Você digitou os números:')
for c in tupla:
    print(c, end=' ')

print(' ')

print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in (n1, n2, n3, n4):
    print(f'O número 3 foi digitado pela primeira vez na {tupla.index(3)+1}° posição')
else:
    print('Não existe o número 3 na lista')

print('Os números pares digitados foram:')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

