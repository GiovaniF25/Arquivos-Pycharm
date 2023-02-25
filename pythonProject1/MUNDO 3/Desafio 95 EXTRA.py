cadastro = {}
dados= []


while True:
    nome = str(input(f' Nome:'))
    cadastro['Nome'] = nome
    idade = int(input(f'Idade: '))
    cadastro['Idade'] = idade
    dados.append(cadastro.copy())    # PRECISO DEIXAR ESSE COPY QUANDO JOGO UM DICIONARIO DENTRE DE UMA LISTA, deixa só uma vez no final
    continuar = str(input('Voce deseja cadastrar mais uma pessoa? digite S para sim e N para não: ')).upper().strip()
    if continuar == 'N':
        break

print('-=' * 25)
print(f' Código  {"Nome":<18} {"Idade":<17}')
print('-'*50)

for k,v in enumerate(dados):
    print(f' {k+1:>02} ',end='')
    for d in v.values():
        print(f' {str(d):<18}',end='')
    print()

soma = 0
for k in dados:
    soma += k['Idade']
print(f'A soma das idades das pessoas cadastradas é {soma} anos ')

