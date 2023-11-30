# Tuplas - IMUTÁVEIS

lanche = ('Hamburger', 'pizza', 'pudim')
print(f'{lanche}')
print('Vou comer muito!')

print(' ')
# olha a diferença na hora de rodar o programa do exemplo de cima com o de baixo, muda a forma de visualização:

lanche = ('Hamburger', 'pizza', 'pudim')
for c in lanche:
    print(f' Eu vou comer {c}')
print('Vou comer muito!')

print(' ')

# posso usar o RANGE dessa forma que o resultado será o mesmo que do programa a cima:
for c in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[c]}')  # aqui ele me mostra todos os elementos
print('Vou comer muito!')

print(' ')
for c in range(0, len(lanche)):
    print(c)   # aqui ele vai me mostrar apenas a quantidade 0,1,2 de elementos (desconsiderando o ultimo elemento)

# COLOCANDO POSIÇÃO
print(' ')

for c in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[c]}, na posição {c}')  # aqui ele me mostra todos os elementos e indica a posição
print('Vou comer muito!')

# OUTRA MANEIRA DE FAZER A MESMA COISA QUE EM CIMA:

print(' ')
for posicao, c in enumerate(lanche):
    print(f'Vou comer {c} na posição {posicao}')
print('Vou comer muito!')

print(' ')
print(' ')
print(' ')

# CRIANDO TUPLAS COM NÚMEROS AGORA
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
c1 = b + a
print(c)
print(c1)
print(len(c)) # contando quantos números tem na tupla
print(c.count(5)) # contando quantas vezes tem o número 5
print(c.index(8)) # mostra a posição do 8
print(c.index(5, 1)) # esse 1 depois do 5 quer dizer que ele vai mostrar a posição depois do número que está na primeira posição

pessoa = ('Giovani', 39, 'M', 85)
# del(pessoa) # se eu colocar del(pessoa) ele ai DELETAR TODA A MINHA TUPLA
# del(pessoa[5]) # nao funciona pq a tupla é imutável, nao consigo alterar nem deletar algo da tupla escrevendo nas linhas abaixo, somente na linha que eu criei a TUPLA
print(pessoa)

# posso colocar tanto letras quanto números nas TUPLAS
