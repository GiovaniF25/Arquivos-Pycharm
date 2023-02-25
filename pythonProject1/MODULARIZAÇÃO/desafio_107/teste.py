# Crie um modulo chamado moeda.py que tenha as funcoes incoporadoras aumentar(diminuir), dorar() e metade()
# faça também um programa que importe esse módulo e use algumas dessas funções

from MODULARIZAÇÃO.desafio_107 import moeda
# NOTE QUE QUANDO EU TENHO PASTAS DENTRO DE PASTAS EU COLOCO UM PONTO, DESSA MANEIRA

p = float(input('Digite o preço: R$'))
x = float(input('Digite o percentual de aumeto (%):'))
print (f'Diminuindo {x}% sobre R${p} o valor será de {moeda.diminuir(p, x)}')

print (f'Aumentando {x}% sobre R${p} o valor será de {moeda.aumentar(p, x)}')
print (f'O dobro de R${p} é {moeda.dobro(p)}')
print (f'A metade de R${p} é {moeda.metade(p)}')

#OU
from moeda import diminuir, metade, dobro, aumentar

p = float(input('Digite o preço: R$'))
x = float(input('Digite o percentual de aumeto (%):'))
print (f'Diminuindo {x}% sobre R${p} o valor será de {diminuir(p, x)}')

print (f'Aumentando {x}% sobre R${p} o valor será de {aumentar(p, x)}')
print (f'O dobro de R${p} é {dobro(p)}')
print (f'A metade de R${p} é {metade(p)}')



