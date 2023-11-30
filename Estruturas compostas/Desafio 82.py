# Crie um programa que vai ler vários números e colocar em uma lista
# Depois mostre a lista, lista com números pares e lista com números ímpares


lista_num = []
lista_pares = []
lista_impares = []

while True:
    n = int(input('Digite um número: '))
    lista_num.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    if n % 2 == 1:
        lista_impares.append(n)
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r not in 'SN':
        while r not in 'SN':
            r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if 'S' not in r:
        break

print(f'A lista completa dos números é {lista_num}')

print(f'A dos números pares é: {lista_pares}  ')

print(f'A dos números ímpares é: {lista_impares}  ')

