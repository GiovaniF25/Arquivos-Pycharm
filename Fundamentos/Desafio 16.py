#Crie um programa que leia um númeor real qualquer e mostre sua porção inteira

from math import trunc

num = float(input('Digite um número qualquer: '))

print('o Valor digitado foi {}, e a porção inteira é {}'. format(num,trunc(num))) #trunc vai mostrar somente a parte inteira



