# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados dados em um dicionário e todos os dicionarios em uma lista
# No final mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade
# c) Uma lista com mulheres
# d) Uma lista com idade acima da média
# e) Quem é a pessoa mais velha do grupo e qual a sua idade

lista_nome = []
lista_sexo = []
lista_idade = []
lista_mulheres = []
lista_idade_acima_da_media = []

print('Cadastro')
while True:
    # nome:
    nome = str(input('Digite o seu nome: '))
    lista_nome.append(nome)
    # sexo:
    while True:
        sexo = str(input('Digite o seu sexo [M/F]: ')).upper()[0]
        if sexo not in 'MF':
            print('Erro! Digite M para masculino e F para feminino: ')
        else:
            break
    lista_sexo.append(sexo)
    if 'F' in sexo:
        lista_mulheres.append(nome)
    # idade:
    idade = int(input('Digite a sua idade: '))
    lista_idade.append(idade)

    # mais cadastros?
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()
        if continuar not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            break
    if continuar in 'Nn':
        break
# a)
if len(lista_nome) <= 1:
    print(f'Foi cadastrado {len(lista_nome)} pessoa')
if len(lista_nome) >= 1:
    print(f'Foram cadastradas {len(lista_nome)} pessoas')
# b)
idade_media = sum(lista_idade) / len(lista_nome)
print(f'A idade média de idade dos cadastrados é de {idade_media} anos')
# c)
if len(lista_mulheres) == 0:
    print('Não existem mulheres na lista')
if len(lista_mulheres) <= 1:
    print(f'A mulher da lista é {lista_mulheres}')
if len(lista_mulheres) > 1:
    print(f'As mulheres da lista são {lista_mulheres}')
# d)
for c in lista_idade:
    if c > idade_media:
        lista_idade_acima_da_media.append(lista_nome[c]) #arrumar essa linha
if len(lista_idade_acima_da_media) <= 1:
    print(f'A  pessoa que tem idade acima da média é: {lista_idade_acima_da_media}')
if len(lista_idade_acima_da_media) > 1:
    print(f'As pessoas com idade acima da média são: {lista_idade_acima_da_media}')
#e)
print(f'A pessoa mais velha do grupo é {lista_nome[lista_idade.index(max(lista_idade))]} e tem {max(lista_idade)} anos')

