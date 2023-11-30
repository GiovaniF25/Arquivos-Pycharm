# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario_1 = {}

dicionario_1['nome'] = str(input('Digite o seu nome:'))
dicionario_1['media']= int(input(f'Digite a sua média do {dicionario_1["nome"]}:' ))

if dicionario_1['media'] >= 7:
    dicionario_1['situação'] = 'Aprovado'
elif 5 <= dicionario_1['media'] < 7:
    dicionario_1['situação'] = 'Recuperação'
elif dicionario_1['media'] < 5:
    dicionario_1['situação'] = 'Reprovado'

print(dicionario_1)

for k,v in dicionario_1.items():       #k é para chave (nesse caso o indice em lista[0,1...] e v para valor = tua expressão
    print(f' {k} : {v}')