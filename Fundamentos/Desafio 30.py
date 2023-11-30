# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

numero=float(input('Digite um número: '))
resultado = numero % 2  # o % significa a sobra de uma divisão. ex 3/2, pensa na conta de divisão, no resto sobra 1, se for 2/2, o resto vai ser zero

if resultado == 0:
    print('O número escolhido é par')
else:
    print('O número é impar')