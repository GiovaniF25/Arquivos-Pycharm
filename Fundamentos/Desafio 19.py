# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Crie um programa que leia os seus nomes
# e sorteie um deles

import random

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

lista = [n1,n2,n3,n4]  # aqui coloca o [] pq é pra lista, e pro python lista se escreve assim
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'. format(escolhido))

# random.randint é um sorteio aleatório, aqui no caso ele vai sorter um número de 1 a 10
print(random.randint(1,10))