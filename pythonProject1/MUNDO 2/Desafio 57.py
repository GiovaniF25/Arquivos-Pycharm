# Faça um programa que leia o sexo de uma pessoa, mas que só aceito 'MASCULINO' ou 'FEMININO' como resposta:

sexo = str(input('Digite o seu sexo:')).upper().strip()
while sexo != 'MASCULINO' and sexo != 'FEMININO':
    sexo = str(input('Digite o seu sexo novamente:')).upper().strip()
print('fim')