#MODULARIZAÇÃO

import uteis

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {uteis.fatorial(n)} e o dobro é {uteis.dobro(n)}')

# ou

from uteis import fatorial, dobro

n = int(input('Digite um número: '))
fat = fatorial(n)
print(f'O fatorial de {n} é {fat} e o dobro é {dobro(n)}')

from importacoes import numeros

n = int(input('Digite um número: '))
fat = numeros.fatorial(n)
print(f'O fatorial de {n} é {fat} e o dobro é {numeros.dobro(n)}')