# Crie um programa que leia vários números inteiros pelo teclado,
# o programa só vai parar quando o usuário digitar o n 999
# No final, mostre quantos números foram digitados e suas somas

soma = contador = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'Foram digitados {contador} números até ser digitado o 999 e sua soma deu {soma}')