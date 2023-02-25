# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar um triângulo ou não

r1= float(input('Digite o comprimento da primeira reta (em metros): '))
r2= float(input('Digite o comprimento da segunda reta (em metros): '))
r3= float(input('Digite o comprimento da terceira reta (em metros): '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')