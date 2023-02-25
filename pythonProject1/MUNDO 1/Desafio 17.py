# Faça um programa que leia o comprimento do cateto oposto e cateto adjacente e mostre qual é a hipotenusa

co = float(input('Insira o comprimento do cateto oposto'))
ca = float(input('Insira o comprimento do cateto adjacente'))

h= (co*co + ca*ca)**(1/2)

print('A hipotenusa do cateto oposto {} e do cateto adjacente {} é de {}:'.format(co,ca,h))