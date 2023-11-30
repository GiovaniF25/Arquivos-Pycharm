# Crie um programa que leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada
# o programa deverá perguntar se o usuário quer ou nao continuar. No final mostre:
# - quantas pessoas tem mais de 18 anos
# - quantos homens foram cadastrados
# - quantas mulheres tem menos de 20 anos


contador_idade = contador_sexo = contador_idade_sexo = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while sexo not in 'M/F':
        sexo = str(input('Digite novamento o sexo [M/F]: ')).strip().upper()[0]

    continuar = str(input('Quer cadastrar mais alguma pessoa? [S/N]: ')).strip().upper()[0]

    if idade > 18:
        contador_idade += 1
    if sexo in 'M':
        contador_sexo += 1
    if idade < 20 and sexo in 'F':
        contador_idade_sexo += 1

    if continuar not in 'S':
        break
print(f'Foram cadastrados {contador_idade} pessoas com mais de 18 anos, um total de {contador_sexo} homens e {contador_idade_sexo} mulheres com menos de 20 anos')
