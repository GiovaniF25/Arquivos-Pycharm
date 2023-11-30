# Faça um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio()
# e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
from random import randint

def sorteio(lista):
    for contador in range(0,5):
        sorteio = randint(1,10)
        numeros.append(sorteio)
    print(f'{numeros}')

def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f' Somando os valores pares, temos {soma}')

numeros = []
sorteio(numeros)
soma_par(numeros)
