# (OBS:) Modificação de enunciado
# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final mostre:
# Mostre caso não exista mulher ou homem na lista
# Qual é a média de idade do grupo
# Quantas pessoas tem no menos de 20 anos

# ao inves de fazer:
#nome =(str(input('Qual é o seu nome?: ')))
#lista_nome.append(nome)
# eu posso fazer simplismente:
#lista_nome.append(str(input('Qual é o seu nome?: ')))

print('=-='*20)
print(' '*5,'Lendo o nome, idade e sexo de quatro pessoas:')
print('=-='*20)

soma_idade = 0
idade_menores20 = 0
lista_nome = []
lista_idade = []
lista_sexo = []

for c in range(2):
    print(f'{c+1}° pessoa: ')
    lista_nome.append(str(input('Qual é o seu nome?: ')))  # aqui eu posso deixar assim, nao tem nenhuma outra informação que depende de um item dentro dessa lista, ai eu ja deixo a própria lista, sem adicionar item por item

    idade = int(input('Qual é a sua idade?: '))         # esse eu deixei assim pq eu quero somar as idades
    lista_idade.append(idade)
    soma_idade += idade

    sexo = str(input('Qual é o seu sexo?: ')).upper().strip()   #aqui eu deixei assim por causa do upper e do strip
    lista_sexo.append(sexo)

    # caso eu nao precise somar algo, ou nao precise colocar upper e strip, posso deixar o append logo na primeira linha
    if idade < 20:
        idade_menores20 += 1
    if 'F' not in lista_sexo:
        print('Não existem mulheres na lista')
    if 'M' not in lista_sexo:
        print('Não existem homens na lista')

print(f'A média de idade das pessoas é {format(sum(lista_idade)/len(lista_idade))}')
print(f'Existem {idade_menores20} pessoas com menos de 20 anos nessa lista')



