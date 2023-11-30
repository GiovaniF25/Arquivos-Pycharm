# Faça um programa que leia um ângulo e mostre o seu seno, cosseno e tangente

import math

a = float(input('Digite um ângulo: '))
s= math.sin(math.radians(a))
c= math.cos(math.radians(a))
t= math.tan(math.radians(a))
print('o seno, cosseno e tangente do angulo {} é {:.2f}, {:.2f} e {:.2f}'. format(a,s,c,t) )