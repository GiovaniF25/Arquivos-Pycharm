# Crie um programa que gerencie o aproveitamento de um jogador de futebol, O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = {}
lista_gols = []
total_gols = []

jogador['Nome do jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome do jogador"]} jogou?:'))

for c in range(0, partidas):
    gols = int(input(f'Quantos gols o {jogador["Nome do jogador"]} fez na partida {c+1}: '))
    lista_gols.append(gols)
    jogador['gols'] = lista_gols
    total_gols = sum(lista_gols)
    jogador['total gols'] = total_gols

print(jogador)
print('=-='*10)
for k, v in jogador.items():
    print(f' {k} : {v}')
print('=-='*10)
print(f'{jogador["Nome do jogador"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f' na {c+1}° partida ele marcou {lista_gols[c]}')

