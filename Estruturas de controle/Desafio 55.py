# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos

lista = []
for p in range(1, 6):
    peso = (input('Digite o peso de {}° pessoa: '.format(p)))
    lista.append(peso)

print('O maior peso é', max(lista))
print('O menor peso é', min(lista))

# uso do append e do extend
# palavras = []
# palavras.append("chocolate")
# print palavras
# ['chocolate']

# palavras = []
# palavras.extend("chocolate")
# print palavras
# ['c', 'h', 'o', 'c', 'o', 'l', 'a', 't', 'e']





