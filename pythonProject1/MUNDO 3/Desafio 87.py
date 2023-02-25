# Aprimore o desafio anterior e mostre:
# - a soma de todos os valores pares
# - a soma dos valores da terceira coluna
# - o maior valor da segunda linha

print('=-='*10)
print(' '*8,'Matriz 3x3')
print('=-='*10)

matriz = [[], [], [], [], [], [], [], [], []]
pares = []
soma = 0
soma_terceira_coluna = 0
maior_segunda_coluna = []

for c in range(9):
    num = (int(input('digite um valor: ')))
    matriz[c].append(num)

    if num % 2 == 0:
        pares.append(num)
        soma += num

    if c == 2  or c == 5 or c == 8:
        soma_terceira_coluna += num

    if c == 3  or c == 4 or c == 5:
        maior_segunda_coluna.append(num)

print('Matriz')
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
print('=-='*10)
print(f' A soma dos números pares da matriz são {soma}')
print(f' A soma dos números da terceira coluna da matriz são {soma_terceira_coluna}')
print(f' O maior valor da segunda linha é {max(maior_segunda_coluna)}')