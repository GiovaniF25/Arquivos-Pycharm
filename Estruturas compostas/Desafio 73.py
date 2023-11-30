# Crie uma tupla preenchida com os 20 primeiros colocados do brasileirão na ordem de colocação
# Depois mostre:
# -Os 5 primeiros colocados
# -Os 4 úlitmos colocados
# -Os times em ordem alfabética
# -Em que posição está o time da Chapecoense

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atéltico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba',
         'Avai', 'Ponte Preta', 'Atlético-GO')
print('Tabela Brasileirão')
for posicao, c in enumerate(times):     #coloco o item posição pq quando eu crio o enumerate ele deixa os itens da lista com numeros ao lado, ex 0 coritnians, 1 palmeiras...
    print(f'{posicao+1}){c}')

# for c in enumerate(times):
#     print(f'{c}')   assim ele só deixa em ordem, mas sem a posição ao lado 1), 2) etc
print('=-='*20)

print(f'Os cinco primeiros colocados são {times[0:5]}')
print('=-='*20)

print(f'Os quatro últimos colocados são {times[-4:20]}') # OU PODE SER [-4:] SE EU NAO COLOCAR NADA ELE VAI ATÉ O FINAL
print('=-='*20)

print(f'Times em ordem alfabética: {sorted(times)}')
print('=-='*20)

print('A posição do time da chapecoense é: {}° lugar'.format(times.index('Chapecoense')+1))
print('=-='*20)


