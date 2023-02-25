# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida:
# media abaixo de 5,está reprovado
# media entre 5 e 6,9 recuperação
# media maior que 7 aprovado

n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite a sua segunda nota'))
media = (n1+n2)/2

if media < 5:
    print('Você está reprovado')
elif media > 5 and media < 6.9:
    print('Você está de recuperação')
elif media >= 7:
    print('Você passou')
