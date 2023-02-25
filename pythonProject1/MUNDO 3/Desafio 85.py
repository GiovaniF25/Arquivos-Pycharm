# Crie um programa onde o usuário possa digitar sete valores númericos
# Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares
# No final, mostre os valores pares e ímpares em ordem crescente

lista_pares = []
lista_impares = []

print('Digite 7 números')
for c in range(7):
    numeros = int(input(f'Digite o {c+1}° número:'))
    if numeros % 2 == 0:
        lista_pares.append(numeros)
        lista_pares.sort()

    if numeros % 2 != 0:
        lista_impares.append(numeros)
        lista_impares.sort()

print(f'Os números pares digitados foram :{lista_pares}, totalizando {len(lista_pares)} números')
print(f'Os números ímpares digitados foram :{lista_impares}, totalizando {len(lista_impares)} números')

