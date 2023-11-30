# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados dados em um dicionário e todos os dicionarios em uma lista
# No final mostre todos os dados do cadastro

dicionario = {}
lista = []

print('Cadastro')
while True:
    dicionario['Nome'] = str(input('Digite o seu nome: '))
    while True:
        dicionario['Sexo'] = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
        if dicionario['Sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    dicionario['Idade']=int(input('Digite o sua idade: '))
    lista.append(dicionario.copy())
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            break
    if continuar in 'Nn':
        break
for c in lista:
    for k,v in c.items():
        print(f' {k} : {v}')



