# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final mostre:
# Qual é a média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem no menos de 20 anos


lista_nome = []
lista_idade = []
lista_sexo = []
lista_nome_homem_mais_velho = []
lista_idade_homem_mais_velho = []
lista_mulheres_menos_de_20 = []
soma_idades = 0

for c in range(4):
   print('{}° pessoa'.format(c))

   nome = str(input('Digite o seu nome: ')). lower().strip()
   lista_nome.append(nome)

   idade = int(input('Digite a sua idade: '))
   lista_idade.append(idade)

   sexo = str(input('Digite o seu sexo:[M/F] ')).upper()
   lista_sexo.append(sexo)

   soma_idades += idade

   if 'M' in sexo:
      lista_nome_homem_mais_velho.append(nome)
      lista_idade_homem_mais_velho.append(idade)

   if 'F' in sexo and idade < 20:
      lista_mulheres_menos_de_20.append(idade)

print('A idade média do grupo é {} anos:'.format(soma_idades/c))

if 'M' in lista_sexo:
   print('O nome do homem mais velho é {}'.format(lista_nome_homem_mais_velho[lista_idade_homem_mais_velho.index(max(lista_idade_homem_mais_velho))]))
else:
   print('Não existe homem na lista')

if 'F' in lista_sexo:
   print('Existem {} mulheres abaixo de 20 nos'.format(len(lista_mulheres_menos_de_20)))
else:
   print('Não existem mulheres na lista')










