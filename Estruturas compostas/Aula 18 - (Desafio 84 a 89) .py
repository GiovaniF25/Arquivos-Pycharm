# Lista parte 2

dados = list() #ou dados = []
dados.append('pedro')
dados.append(25)
print(dados[0])
print(dados[1])
print(dados)

# declarando lista dentro de listas

pessoas = list()
pessoas.append(dados[:])
print(pessoas) #assim eu deixei uma lista dentro de outra lista

pessoas = [['Pedro', 25], ['Maria',10],['João',25]]  #lista dentro de listas, em ordem, 0,1 e 2
print(pessoas)
print(pessoas[0][0]) # aqui dentro de pessoas 0 (pedro,25) eu peguei o item 0, Pedro, assim só aparece o pedro

teste = []
teste.append('Giovani')
teste.append(25)

galera = []
galera.append(teste[:])  #eu preciso deixar esse [:] para criar um lista dentro de outra lista

teste[0] = 'Eduarda'  #coloco isso pra mudar o item 0
teste [1] = 20        #coloco isso pra mudar o item 1
galera.append(teste[:])
print(galera)
print('------')
galera = [['João', 25], ['Giovani', 26], ['Eduarda', 20]]
for c in galera:
    print(c)
    print(c[0])
    print(c[1])
    print('--')
    print(f' {c[0]} tem {c[1]} anos de idade')

print('----------')
galera = []
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)