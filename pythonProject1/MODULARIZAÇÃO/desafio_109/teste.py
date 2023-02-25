# melhorei o desafio anterior colocando às vírgulas e duas casas decimais para os valores

from MODULARIZAÇÃO.desafio_109 import moeda

p = float(input('Digite o preço: R$'))
x = float(input('Digite o percentual de aumeto (%):'))
print (f'Diminuindo {x}% sobre {(p)} o valor será de {(moeda.diminuir(p, x, True))}')

print (f'Aumentando {x}% sobre {(p)} o valor será de {(moeda.aumentar(p, x, True))}')
print (f'O dobro de {(p, True)} é {(moeda.dobro(p, True))}')
print (f'A metade de {(p, True )} é {(moeda.metade(p, True))}')

