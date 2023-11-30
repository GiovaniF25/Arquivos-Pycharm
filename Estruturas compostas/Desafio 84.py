# Faça um programa que leia o nome e o peso de pelo menos 2 pessoas, guardando em uma lista
# No final mostre quantas pessoas foram cadastradas

dados = []
lista = []

# to inserindo 2 coisas diferentes numa mesma lista, antes eu inseria um item e dava append, agora tenho variáveis diferentes
for c in range(2):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    lista.append(dados[:]) # se eu colocar uma lista dentro de uma lista eu preciso dos [:], se eu criar uma variavel que nao seja lista, e quero deixar ela como lista dentro de outra, ei só escrevo o nome dela e coloco os []
    dados.clear()      # eu uso o clear pra pq por ex: se eu cadastar gio 100kg e duda 60kg e eu usar o clear vai ficar (gio, 100) (duda 60)
                       # caso eu nao usasse o clear iria ficar (gio,100) (gio,100 duda,60) e assim sucessivamente conforme eu for colocando dados

continuar = str(input('Deseja continuar cadastrando pessoas? Digite [S] para sim ou [N] para não.')).upper().strip()
if continuar not in 'SN':
    while continuar not in 'SN':
        continuar = str(input('Digite novamente. continuar cadastrando pessoas? Digite [S] para sim ou [N] para não.')).upper().strip()

while 'S' in continuar:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar cadastrando pessoas? Digite [S] para sim ou [N] para não.')).upper().strip()

if 'N' in continuar:
    print(lista)
    print(f' Você cadastrou {len(lista)} pessoas')







