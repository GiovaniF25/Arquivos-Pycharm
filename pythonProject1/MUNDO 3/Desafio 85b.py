# Resolução Guanabara (colocando lista dentro de listas)

# Crie um programa onde o usuário possa digitar sete valores númericos
# Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares
# No final, mostre os valores pares e ímpares em ordem crescente

listas = [[],[]] # criei uma lista com duas listas dentros

print('Digite 7 números')
for c in range(7):
    numeros = int(input(f'Digite o {c+1}° número:'))
    if numeros % 2 == 0:
        listas[0].append(numeros)      # se o número for divisível por 2 ele vai adicionar o 1° elemento da lista
        listas[0].sort()
    if numeros % 2 != 0:
        listas[1].append(numeros)       # se o número for divisível por 2 ele vai adicionar o 2° elemento da lista
        listas[1].sort()

print(f'Os números pares digitados foram {listas[0]}, totalizando {len(listas[0])} números')
print(f'Os números ímpares digitados foram {listas[1]}, totalizando {len(listas[1])} números')