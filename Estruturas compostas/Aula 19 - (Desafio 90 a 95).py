# Dicionários

# diferença de dicionários para as tuplas e listas é que eu posso usar "palavras" para identificar um item,
# e não só item 0, 1, 2
# ex:
lista_1 = ['Bolsonaro']
print(lista_1[0]) # vai aparecer só o bolsonaro

# com o dicionário eu posso escreve dessa forma:
dicionario_1 = {'presidente': 'Bolsonaro'}
print(dicionario_1['presidente']) #aqui se fosse lista eu colocaria o [0], mas no dicionário voce escreve a value
print(dicionario_1) #assim ele mostra tudo entre meio os {}

for k,i in dicionario_1.items():
    print(f'{k}: {i}') #assim ele mostra tudo sem os {}

print('=-='*30)
filme = {'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'}

print(filme.values()) # vai pegar Star Wats, 1997 e George Lucas
print(filme.keys()) # vai pegar titulo, ano e diretor
print(filme.items()) # vai aparecer tudo

for k,v in filme.items():
    print(f' O {k} é {v}')

# pra adicionar um elemento em dicionário é só escrever:
filme['tipo'] = 'Terror' # nao precisa do append
print(filme)

# pra tirar é só colocar del
del filme['tipo']
print(filme)

print('=-='*30)
# posso criar uma lista onde cada elemento tem um dicionário dentro
# assim como eu podia criar uma lista onde cada elemento seja outra lista dentro

pessoas = {'nomes': 'Giovani', 'sexo': 'masculino', 'idade': '25'}
print(pessoas)
print(f' O {pessoas["nomes"]}, tem {pessoas["idade"]} anos')      #aqui cuida que "nomes" e "idade" tem que ter aspas duplas pq ja tem aspas simples no começo

estado = {}
brasil = []

for c in range(2):
    estado['UF'] = str(input('Unidade federativa:'))
    estado['Sigla'] = str(input('Sigla'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end='')


print('-'*50)
#DICIONÁRIO SEM REPETIÇÃO WHILE E FOR, NAO PRECISO CRIAR UMA LISTA PRA MOSTRA-LO, SÓ MOSTRO POR FOR K, V IN DICIONARIO.ITEM()

#SE EU TIVER USANDO FOR E WHILE PARA REPETIÇÃO COM A FINALIDADE DE GUADAR MAIS QUE UM DADO EU PRECISO DE UMA LISTA PARA PODER VISUALIZAR AS INFORMAÇÕES ADICIONADAS NO DICIONÁRIO, SE EU COLOCAR SÓ O FOR K, V IN DICIONARIO.ITEM() ELE SÓ VAI MOSTRAR O ULTIMO ITEM, POR ISSO PRECISO DA LISTA PARA VISUALIZA-LÁ
#PARA RETIRAR INFORMAÇÕES DA LISTA:
#USAR O FOR IN LISTA PARA MOSTRAR TUDO O QUE FOI COLOCADO DENTRO DO DICIONÁRIO, SE NAO USAR O FOR IN LISTA, ELE VOU MOSTRAR SOMENTE O ULITMO ITEM ADICIONADO NO DICIONARIO
#EX:
cadastro = {}
dados = []

for c in range(5):
    idade = int(input(f'Digite a idade da {c+1}° pessoa: '))
    cadastro['Idade'] = idade
    dados.append(cadastro.copy())       # PRECISO DEIXAR ESSE COPY QUANDO JOGO UM DICIONARIO DENTRE DE UMA LISTA

soma = 0
for c in dados:
    soma += c['Idade']
print(f' A soma das idades é de {soma} anos')
