#continuação de função

help() # é digitado para tirar uma dúvida, da um RUN e escreve o comando que vc tem dúvida
help(print) # ao inves de escrever minha função lá em baixo no RUN, eu posso colocar hel("funcao que tenho duvida"), vai aparecer direto dai

def contador(i,f,p):
    contagem = i
    while contagem <= f:
        print(f'{contagem}', end='')
        contagem += p
    print('FIM')
contador(2,10,2)

# supondo que eu nao sei que contador(2,10,2), eu posso utilizar o
def contador(i,f,p):
    """      # eu coloco 3 aspas duplas e clico no enter em cima, ele vai mostrar o que é o i,f,p

    :param i: #aqui eu digito o que eu quero dai
    :param f:
    :param p:
    :return:
    """
help(contador)

# parametro funcional
def somar(a,b,c):
    s = a+b+c
    print(f'A soma vale {s}')
somar(3,2,5)
somar(8,4) # se eu colocar isso no programa vai dar erro, preciso de 3 parametros

def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale {s}')
somar(3,2,5)
somar(8,4) # se eu colocar isso no programa vai dar erro, preciso de 3 parametros
# dessa forma vai rodar pq coloquei c=0 aqui SE NÃO TIVER NADA NO C, ele vai considerar 0 e vai funcionar

# escopo de variáveis
# ex: (cuidar o alinhamento do numero pra ver se é global ou local
#n = 2 a posição é de variável global - escopo global
    #x =3 a posição é de variável local - escopo local


