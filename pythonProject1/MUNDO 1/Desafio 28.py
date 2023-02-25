# Escreva um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário tentar descorir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se  usuário venceu ou não

import time
import random

computador= random.randint(0,5)

print('''         Vamos jogar um jogo? 
         Pense em um número inteiro entre 0 e 5''')
print('Pensou?')
print('Vamos ver se foi o mesmo número escolhido pelo computador?')

jogador= int(input('Digite o número que você pensou: '))
print('PROCESSANDO...')
time.sleep(2)
print('O número escolhido pelo computador foi: {}'.format(computador))
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')


