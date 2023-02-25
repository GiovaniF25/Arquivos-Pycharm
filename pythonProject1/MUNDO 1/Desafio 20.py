# O mesmo professor quer sortear a ordem de apresentação de seus alunos. Faça um programa que leia o nome dos alunos
# e mostre a ordem sorteada

import random

n1= str(input('primeiro aluno'))
n2= str(input('segundo aluno'))
n3= str(input('terceiro aluno'))
n4= str(input('quarto aluno'))

lista= [n1,n2,n3,n4]
random.shuffle(lista)  #shuffle significa embaralhar

print('A ordem de apresentação é {}'. format(lista))