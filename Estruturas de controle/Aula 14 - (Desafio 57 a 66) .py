# estrutura de repetição WHILE (usando quando eu SEI e quando eu NAO SEI o limite)
# o FOR eu só uso quando eu sei o limite

for c in range(1, 11):
    print(c, end=' ')
print('fim')

# posso fazer dar o mesmo resultado fazendo o while desse jeito:
c = 1  # aqui o c = 1 pq o primeiro termo vai ser 1
while c < 11:
    print(c, end= ' ')
    c += 1
print('fim')

# exemplo de situações que eu tenho um limite, nao sei quando termina
# Aqui por exemplo, o meu limite é chegar no SIM, pode ser na primeira digitada ou na milésima

r = 'SIM'
while r == 'SIM':
    r= str(input('Digite um valor: ')).upper()
print('fim')

n = 1 # ISSO AQUI É GAMBIARRA, QUANDO TEM NÚMERO COLOCA ESSA 1 NA FRENTE
par = 0
impar = 0
while n != 0:
    n = (int(input('Digite um valor: ')))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} números pares e {} números impares'.format(par, impar))



