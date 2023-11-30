# Crie um programa que tenha uma tupla com várias palavras (nao usar acentos). Depois disso
# você deverá mostrar, para cada palavra quais são as vogais:

palavras = ('aprender', 'programar', 'python', 'curso', 'Giovani', 'Eduarda')

for c in palavras:
    print(f'\n Na palavra {c} temos as vogais:', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')