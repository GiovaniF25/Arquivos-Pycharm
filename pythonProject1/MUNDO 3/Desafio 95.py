# Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes de aproveitamento de cada jogador:

player = {}
gols = []
campeonato = []
contP = 0
print('-'*40)
# Cadastramento
while True:
    player['Nome'] = str(input('Nome: '))
    contP = int(input(f'Quantas partida {player["Nome"]} jogou? '))
    for p in range(0,contP):
        gols.append(int(input(f'Número de gols na partida {p+1}: ')))
    player['Gols'] = gols.copy()
    player['Total'] = sum(gols)
    campeonato.append(player.copy())

    resp = str(input('Continuar[s/n]?  '))
    if (resp).lower() == 'n':
        break

# Listagem dos dados cadastrados
print('-=' * 25)
print(f' Cod  {"Nome":<18} {"Gols":<17}{"Total":<18} ')
print('-'*50)
for m,x in enumerate(campeonato):
    print(f' {m+1:>02} ',end='')
    for d in x.values():
        print(f' {str(d):<18}',end='')
    print()
print('-='*25)
# Detalhamento do Cadastro
while True:
    num = int(input('Quer ver dados de que jogador? [Cod - 999 encerra]: '))
    if num == 999:
        break
    while num not in range(0,len(campeonato)+1):
        print(f'>>>> jogador inválido - Jogadores de 1 a {len(campeonato)}:')
        num = int(input('Quer ver dados de que jogador? [Cod - 999 encerra]: '))
    print('-'*50)
    print(f'-- DADOS DO JOGADOR {campeonato[num-1]["Nome"]}:')
    for k,v in enumerate(campeonato[num-1]['Gols']):
        print(f'No jogo {k} fez {v} gols.')
    print('-' * 50)
print('<<< ENCERRADO >>>')