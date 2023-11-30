#Se eu fosse somente sortear numeros para mega sena, eu tenha que colocar os numeros aleatórios dentro das listas
# se nao eu só consigo sortear um por vez

from random import randint

jogos = []
contador = 0
while True:
    numero_aleatorio = randint(1, 60)
    if numero_aleatorio not in jogos:
        jogos.append(numero_aleatorio)
        contador += 1
    if contador >= 6:
        break
jogos.sort()

print(f'Sorteando {jogos}')
