


cadastro = {}
dados = []
mulheres = []
acima_media = []

while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if cadastro['Sexo'] not in 'MF':
            print('Digite novamente apenas M para masculino ou F para feminino: ')
        else:
            break
    cadastro['Idade'] = int(input('Idade: '))
    dados.append(cadastro.copy())     # pra eu visualizar os dados do dicionários eu preciso colocar ele dentro de uma lista
    while True:
        continuar = str(input('Voce deseja cadastrar outra pessoa? [S/N]:')).upper()
        if continuar not in 'SN':
            print('Digite novamente apenas S para sim ou N para não')
        else:
            break
    if continuar in 'N':
        break

print(dados)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')

soma = 0
for c in dados:
    soma += c['Idade']
media = soma/len(dados)
print(f'B) A média de idade é de {media} anos')

for c in dados:
    if c['Sexo'] == 'F':
        mulheres.clear()
        mulheres.append(c["Nome"])
        if len(mulheres) != 0:
            print(f'C) As mulheres cadastradas foram {c["Nome"]}')
        else:
            print(f'C) Não existem mulheres na lista')
for c in dados:
    if c['Idade'] > media:
        acima_media.append(c['Nome'])
        print('D) Acima da média de idade:')
        for k, v in c.items():
            print(f' {k} : {v}')
    if c['Idade'] == media:
        print('D) Não tem ninguém acima da média')


print('Fim do cadastro')