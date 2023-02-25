# aprendendo sobre importações de bibliotecas
import math
num= int(input('Digite um número:'))
raiz= math.sqrt(num)
print('A raíz de {} é igual a {}:'.format(num,math.ceil(raiz)))

from math import sqrt
num= int(input('Digite um número:'))
raiz= sqrt(num)
print('A raíz de {} é igual a {}:'.format(num,math.ceil(raiz)))

n=int(input('Digite um número'))
r=n**(1/2)
print('A raíz de {} é igual a {}:'.format(n,r))

# --------------------------------------------------------------------------------------------------
# importação da biblioteca random, usando o randint e o unidecode (que desconsidera os acentos)

import random

num = random.randint(1,10)
print(num)

from unidecode import unidecode

frase = 'A mãe te ama'
print(unidecode(frase))

# --------------------------------------------------------------------------------------------------
# importanto biblioteca de emoji

import emoji
print(emoji.emojize('olá mundo :dizzy:'))