# Crie um programa que faça o computador jogar Jokenpô com você

import random
import time

print('\033[1;32m Ei, computador! Vamos jogar Jokenpô???\033[m')
time.sleep(1.5)

print('Sim? Ok, se prepare!')
time.sleep(1.5)

escolha_jogador = str(input('Vou escolher entre pedra, papel e tesoura: ')).lower().strip()

print('JO')
time.sleep(1.5)
print('KEN')
time.sleep(1.5)
print('PÔ')

n1 = 'pedra'
n2 = 'papel'
n3 = 'tesoura'

lista = [n1,n2,n3]
escolha_computador = random.choice(lista).lower()

print('A escolha do computador foi {}'. format(escolha_computador))
print('A escolha do jogador foi {}'. format(escolha_jogador))

if escolha_jogador == 'pedra' and escolha_computador == 'tesoura':
    print('O computador escolheu {} e eu escolhi {}, Eu venci!'.format(escolha_computador,escolha_jogador))
elif escolha_jogador == 'pedra' and escolha_computador == 'papel':
    print('O computador escolheu {} e eu escolhi {}, O computador venceu!'.format(escolha_computador, escolha_jogador))
elif escolha_jogador == 'pedra' and escolha_computador == 'pedra':
    print('O computador escolheu {} e eu escolhi {}, Deu impate!'.format(escolha_computador,
                                                                                      escolha_jogador))

elif escolha_jogador == 'papel' and escolha_computador == 'tesoura':
    print('O computador escolheu {} e eu escolhi {}, O computador venceu!'.format(escolha_computador, escolha_jogador))
elif escolha_jogador == 'papel' and escolha_computador == 'pedra':
    print('O computador escolheu {} e eu escolhi {}, Eu venci!'.format(escolha_computador, escolha_jogador))
elif escolha_jogador == 'papel' and escolha_computador == 'papel':
    print('O computador escolheu {} e eu escolhi {}, Deu impate!'.format(escolha_computador,
                                                                             escolha_jogador))

elif escolha_jogador == 'tesoura' and escolha_computador == 'pedra':
    print('O computador escolheu {} e eu escolhi {}, O computador venceu!'.format(escolha_computador, escolha_jogador))
elif escolha_jogador == 'tesoura' and escolha_computador == 'papel':
    print('O computador escolheu {} e eu escolhi {}, Eu venci!'.format(escolha_computador, escolha_jogador))
elif escolha_jogador == 'tesoura' and escolha_computador == 'tesoura':
    print('O computador escolheu {} e eu escolhi {}, Deu impate!'.format(escolha_computador,
                                                                             escolha_jogador))

print('Vamos jogar de novo?')