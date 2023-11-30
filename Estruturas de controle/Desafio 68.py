# Faça um programa que jogue par ou ímpar com o computador;
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo

print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-='*10)

import random

contador = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha_jogador = str(input('Escolha se você quer PAR (P) ou ÍMPAR (I): ')).upper().strip()[0]
    computador = random.randint(0, 10)
    total = jogador + computador

    if escolha_jogador not in 'PI':
        while escolha_jogador not in 'PI':
            escolha_jogador = str(input('INVÁLIDO. Escolha se você quer PAR (P) ou ÍMPAR (I): ')).upper().strip()

    if escolha_jogador in 'PI':
        if total % 2 == 0:
            jogada = 'Par'
        elif total % 2 != 0:
            jogada = 'Ímpar'


    print(f'Você escolhou o número {jogador} e o computador escolhou o número {computador}\n'
          f'A soma dos números deu {total} que é um número {jogada}')
    contador += 1
    if escolha_jogador not in jogada:
        break
print(f'fim de jogo, você jogou {contador} vezes e ganhou {contador-1} vezes')




