# Melhor o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import time
import random

print(' Ei, Vamos jogar um jogo? \n Pense num número entre 0 a 10')
time.sleep(1)

escolha_jogador = int(input(' Agora digite o número escolhido e vamos ver se foi o mesmo escolhido pelo computador: '))
escolha_computador = random.randint(0, 10)

contador = 1 # aqui coloca o 1 pq se vc colocar o 0 e acertar na primeira tentativa ele diz que vc acertou na 0 tentativa
while escolha_computador != escolha_jogador:
    escolha_jogador = (int(input('Você errou! tente novamente:')))
    contador = contador + 1
print('Parabéns, você acertou na {} tentativa'.format(contador))




