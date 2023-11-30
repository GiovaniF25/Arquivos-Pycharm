# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma sequencia de fibonacci.

# 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21...
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

numero_escolhido = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end =' ')
t3 = t1 + t2
contador = 3
while contador <= numero_escolhido:
    t3 = t1 + t2
    print('-> {}'.format(t3), end = ' ')
    t1 = t2
    t2 = t3
    contador = contador + 1
print('')
print('Fim')