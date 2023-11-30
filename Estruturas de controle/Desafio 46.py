# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0
# e com pausa de 1 segundo entre eles

from time import sleep
import emoji

print('Contagem regressiva para o estouro dos fogos')
for c in range (10,0,-1):
    print(c)
    sleep(1)
print('\33[31m Booooom \33[m')
print(emoji.emojize(':fire:'*10))