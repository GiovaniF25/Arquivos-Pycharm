# Faça um programa que leia um número inteiro e diga se ele é um número primo

numero = int(input('Digite um número: '))
contagem = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        contagem += 1

print(' ')
print('\033[mO número {} foi dividido {} vezes'.format(numero,contagem))
if contagem == 2:
    print('O número {} é um número primo.'.format(numero))
else:
    print('O número {} não é um número primo.'.format(numero))





