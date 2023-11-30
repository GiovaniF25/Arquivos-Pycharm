# aqui é o mesmo exercício 58 e vai dando informações pro jogador

from random import randint
from time import sleep

print(' Ei, Vamos jogar um jogo? \n Pense num número entre 0 a 10')
sleep(0.1)

escolha_jogador = int(input(' Agora digite o número escolhido e vamos ver se foi o mesmo escolhido pelo computador: '))
escolha_computador = randint(0, 10)

contador = 1
while escolha_jogador != escolha_computador:
    if escolha_computador > escolha_jogador:
        escolha_jogador = int(input(('Você errou, tente um número mais alto: ')))
    elif escolha_computador < escolha_jogador:
        escolha_jogador = int(input(('Você errou, tente um número mais baixo:')))
    contador += 1
    if contador > 5:
        print('Você é muito ruim de chute, mas vamos lá, tente mais uma vez!')

print('Parabéns, voce acertou na {}° tentativa'.format(contador))



