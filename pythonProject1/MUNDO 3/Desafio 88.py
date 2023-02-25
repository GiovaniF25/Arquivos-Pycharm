# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa
# vai perguntar quantos jogos serão gerados e sorteie 6 números entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista

print('-'*30)
print('    JOGUE NA MEGA SENA ')
print('-'*30)

from time import sleep
import random

jogos = []
final = []
condicao = int(input('Quantos jogos vc quer q eu sorteie? '))
total = 1
while condicao >= total:
    contador = 0
    while True:
        numero_aleatorio = random.randint(1, 60)
        if numero_aleatorio not in jogos:
            jogos.append(numero_aleatorio)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    final.append(jogos[:])
    jogos.clear()
    total += 1
print(f'Sorteando {condicao} jogos:')
for i, l in enumerate(final):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)




