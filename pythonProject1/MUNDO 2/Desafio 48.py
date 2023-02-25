# Faça um programa que calcule a soma de todos os números impares que sao multiplos de 3 e que se encontram no
# intervalo de 1 a 500

print('Os números ímpares e múltiplos de 3 no intervalo de 1 a 500 são:')
soma = 0
contador = 0

for intervalo in range(1,501,2):
    if intervalo % 3 == 0:
        soma = soma + intervalo # +=: é equivalente a fazer x = x + valor. Por exemplo, se x valer 10 e fizermos x += 2, x passará a ter o valor 12.
        contador = contador + 1
        print(intervalo, end=' ')
print(' ')
print(' ')

print('A soma dos {} números ímpares e múltiplos de 3 no intervalo de 1 a 500 é {}'.format(contador,soma))
print('FIM')


# soma = 0
# contador = 0
# soma coloca o (C) depois do +=
# contador coloca o += 1


