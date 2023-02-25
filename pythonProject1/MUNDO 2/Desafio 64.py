# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles

contador = 0
soma = 0
n = ''
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
print('Foram digitados {} números até ser digitado o número 999 e a soma entre eles é: {}'.format(contador, soma-999))

#ou
print('----------------------------------------------')

num = soma = 0
cont = 1
while num != 999:
    num = int(input('Digite um número: [999 pra parar] '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} números e a soma foi {}'.format(cont, soma))