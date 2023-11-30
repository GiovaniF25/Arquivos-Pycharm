# estrutura de repetição FOR

# laço c no intervalo(1,10)
# for c in range(1,10)

# c significa variável de controle, mas pode ser qualquer letra
# for significa 'laço'
# in signigica 'no'
# range significa 'intervalo'

# aqui ele conta de 0 a 6
for c in range(0,6):
    print(c)
print('fim 1')
print('')

# aqui ele conta de 0 a 6 ao contrário
for c in range(6,0,-1):
    print(c)
print('fim 2')
print('')

# aqui ele repete o Oi 3 vezes
for c in range(0,3):
    print('Oi')
print('fim 3')
print('')

n = int(input('Digite um número: ')) # ele vai contar de 0 até o número em que eu digitar
for c in range(0,n+1):
    print(c)
print('Fim 4')
print('')

i = int(input('Início'))  # número que eu quero iniciar a contagem
f = int(input('fim'))   # número que eu quero terminar a contagem
p = int(input('passo'))     # ex: se for igual a 2, ele vai contar de 2 em 2

for c in range(i,f+1,p):
    print(c)
print('Fim 5')
print('')

for c in range(0,3):    # aqui ele vai pedir pra digitar um número 3 vezes
    n = int(input('Digite um número'))
print('Fim 6')
print('')

s = 0     # aqui ele vai fazer o somatório dos 4 números, ele colocou o s=0 para nao interferir na soma
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s = (s + n)
print('O somatório de todos os valores foi: {}'.format(s))

#+=: é equivalente a fazer x = x + valor. Por exemplo, se x valer 10 e fizermos x += 2, x passará a ter o valor 12.

# -=, =, /=, //=, %=, *=: funcionam da mesma forma que o +=.
# Por exemplo, se x valer 5 e fizermos x *= 3 obteremos o valor 15. Na prática, o funcionamento desses operadores é o seguinte: x op= valor é equivalente a x = x op valor, em que op é algum dos operadores listados anteriormente.