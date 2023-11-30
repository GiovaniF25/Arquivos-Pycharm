# Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado
# equilátero, escaleno ou isosceles

r1= float(input('Digite o comprimento da primeira reta (em metros): '))
r2= float(input('Digite o comprimento da segunda reta (em metros): '))
r3= float(input('Digite o comprimento da terceira reta (em metros): '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('Os segmentos podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triangulo é equilátero')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r1 != r2 == r3:
        print('O triangulo é escaleno')
    elif r1 != r2 != r3:
        print('O triangulo é isosceles')
else:
    print('Os segmentos não podem formar um triângulo')