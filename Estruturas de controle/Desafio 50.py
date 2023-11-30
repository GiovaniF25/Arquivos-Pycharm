# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado por impar, desconsidere


soma = 0
contador = 0

for c in range(1,7):
    numeros = int(input('Digite o {}° valor: '.format(c)))
    if numeros % 2 == 0:
        soma += numeros
        contador += 1

print('Você informou {} números pares e a soma dos números pares é {}'.format(contador, soma))

