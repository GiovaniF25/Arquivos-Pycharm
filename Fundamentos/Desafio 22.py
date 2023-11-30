# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - escrito e letras maiúsculas e minísculas
# - quantas letras existem no nome completo
# - quantas letras existem no primeiro e segundo nome separadamente

# colocar nome composto
nome =str((input('Digite um nome: ')))
print('Analisando o seu nome:')


print('Seu nome em maiusculo fica: {}'.format(nome.upper()))
print('Seu nome em minusculo fica: {}'. format(nome.lower()))
print('Seu nome tem {} letras:'.format(len(nome))) #assim ele conta os espaços junto
print('Seu nome tem {} letras:'.format(len(nome)-nome.count(' ')))   # aqui ele ta contando as letras do nome, menos os espaço (' ') significa espaço
separa=nome.split()
print('Seu primeiro nome tem é {} e tem {} letras'. format(separa[0],len(separa[0])))
print('Seu segundo nome tem é {} e tem {} letras'. format(separa[1],len(separa[0])))


#posso criar um linha separada e colocar dentro do format, mais assim fica com mais passos ex:

maiscula = nome.upper()
print('Seu nome em maiusculo fica: {}'.format(maiscula))