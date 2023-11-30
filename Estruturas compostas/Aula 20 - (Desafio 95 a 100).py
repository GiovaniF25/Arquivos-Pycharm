#FUNÇAO

# crio uma função para melhor organizar o meu código, e não ficar repetindo muitas linhas iguais
# ex:

print('----')
print('Curso em vídeo')
print('----')
print('Aprenda python ')
print('----')
print('Abençoado')
print('----')

#para eu ter o mesmo resultado que isso, preciso criar funcoes:

def linha():
    print('----')

print('Curso em vídeo')
linha()
print('Aprenda python ')
linha()
print('Abençoado')

# posso não apenas criar uma linha, mas sim deixar um função no meio, ex:
def mensagem(msg):
    print('----')
    print(msg)
    print('----')

mensagem('Sistema de alunos')

# Novo exemplo:
def titulo(txt):
    print('---')
    print(txt)
    print('---')

titulo(' Curso em vídeo')
titulo(' Aprenda python')
titulo(' Abençoado')

#mais exemplos
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

#troca por:
def soma(x,y):
    s = x + y
    print(s)

soma(4,5)
soma(8,9)


# não preciso colocar o x e y lá em baixo antes dos numeros na soma
# mas posso colocar se eu quiser:
def soma(x, y):
    print(f'X = {x} e Y = {y}')
    s = x + y
    print(s)

soma(x=4, y=5)

#EMPACOTAR PARAMETROS
# aqui se eu colocar *núm, eu nao sou obrigado a colocar quantos elementos vao ser inseridos como no ex a cima
# no ex anterior, se eu colocasse soma(1,2,3) ele daria erro, pq eu falei que seria 2, se eu nao sei eu coloco o Núm
def contador(* núm):
    print(núm)

contador(2,1,7)
contador(2)
contador(2,1,7,8,7)

# Usando o for junto com empacotamento, mesma forma de fazer o elemento anterior

def soma (* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}')

soma(5, 2)
soma(5, 2, 9)





#Criar funcoes com LISTAS
def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1

valores = [3,6,9,12]
dobra(valores)
print(valores)


