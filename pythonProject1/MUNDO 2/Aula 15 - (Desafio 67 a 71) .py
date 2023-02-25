# Uso do break

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('a soma vale {}'.format(s-999))

# ou
print('---------')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'a soma vale {s}')

# ao inves do formato usa essa f' {algo}