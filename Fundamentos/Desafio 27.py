# Faça um programa que leia o nome completo de uma pessoa, e mostrando em seguida o último nome de mandeira separada
# ex: Ana Maria (primeiro Ana, segundo Maria)

n= str(input('Digite o seu nome: ')).split()

print('Seu primeiro nome é {}, e seu segundo nome é {}'.format(n[0],n[1]))