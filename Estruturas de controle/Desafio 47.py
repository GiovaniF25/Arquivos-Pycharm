# Crie um programa que conte todos os números pares, que estão no intervalo de 1 a 50

contador = 0
for numero in range(2,51,2):
    contador = contador + 1
    print(numero, end=' ')
print(' ')
print('Existem {} números pares entre 1 e 50'.format(contador))

#ou

print('')
for numero in range(2,51):
    if numero % 2 == 0:
        print(numero, end=' ')
