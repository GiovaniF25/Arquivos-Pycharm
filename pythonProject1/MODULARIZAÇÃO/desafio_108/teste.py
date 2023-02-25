# melhorei o desafio anterior colocando às vírgulas e duas casas decimais para os valores

from MODULARIZAÇÃO.desafio_108 import moeda

p = float(input('Digite o preço: R$'))
x = float(input('Digite o percentual de aumeto (%):'))
print (f'Diminuindo {x}% sobre {moeda.leitura(p)} o valor será de {moeda.leitura(moeda.diminuir(p, x))}')

print (f'Aumentando {x}% sobre {moeda.leitura(p)} o valor será de {moeda.leitura(moeda.aumentar(p, x))}')
print (f'O dobro de {moeda.leitura(p)} é {moeda.leitura(moeda.dobro(p))}')
print (f'A metade de {moeda.leitura(p)} é {moeda.leitura(moeda.metade(p))}')

#OU
from moeda import diminuir, metade, dobro, aumentar, leitura

p = float(input('Digite o preço: R$'))
x = float(input('Digite o percentual de aumeto (%):'))
print (f'Diminuindo {x}% sobre {leitura(p)} o valor será de {leitura(diminuir(p, x))}')

print (f'Aumentando {x}% sobre {leitura(p)} o valor será de {leitura(aumentar(p, x))}')
print (f'O dobro de {leitura(p)} é {leitura(dobro(p))}')
print (f'A metade de {leitura(p)} é {leitura(metade(p))}')