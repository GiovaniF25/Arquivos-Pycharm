# código que faz os jogadores "jogar o dado"

from random import randint
from time import sleep

jogadores = {}
for c in range(1, int(input('quantos jogadores participarão? ')) + 1):
    jogadores[c] = randint(1,6)
    print(f'o jogador {c} tirou {randint(1,6)} no dado')
    sleep(0.75)

# código que pega a variável Jogadores e coloca na variável Ranking ordenado em ordem decrescente
ranking = {}
while len(jogadores) > 0:
    maior = [0, 0]
    for chave, valor in jogadores.items():
        if valor > maior[1]:
            maior = [chave, valor]
    ranking[maior[0]] = maior[1]
    del jogadores[maior[0]]

# código que coloca os jogadores que tiraram a mesma coisa no dado na mesma posição do Ranking
aparecido = list()
for chave, item in ranking.items():
    novo = True
    for item2 in range(0, len(aparecido)):
        if item == aparecido[item2][0]:
            novo = False
            aparecido[item2][1].replace(' e',',')
            aparecido[item2][1] += f' e {chave}'
            break
    if novo:
        aparecido.append([item, str(chave)])

# código que transcreve oque temna variável Aparecido para a variável Ranking
ranking = dict()
for item3 in aparecido:
    ranking[item3[1]] = item3[0]

#código que mostra o Ranking
print('Ranking: ')
posicao = 1
for chave, valor in ranking.items():
    posicao += 1
    sleep(0.75)
    print(f'{posicao - 1}° lugar: jogador {chave} com {valor} pontos')