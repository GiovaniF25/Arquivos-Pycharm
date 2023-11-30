# Crie uma programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tea, com a formatação correta

print('=-='*10)
print(' '*8,'Matriz 3x3')
print('=-='*10)

matriz = [[], [], [], [], [], [], [], [], []]

for c in range(9):
    matriz[c].append(int(input('digite um valor: ')))

print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])


matriz = [[], [], []]
for l in range(3): # l para linha
        for c in range(3): # c para coluna
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)

for l in range(3):
        for c in range(3):
                print(f'[{matriz[l][c]}]', end='')
        print()