# Crie um programa que tenha uma função fatorial() que receba dois parametros, o primeiro que indique o número indique o número
# a calcular e o outro chamado show que será um valor lógico (opcional) indica-se se erá mostrado ou não na tela
# o processo de cálculo fatorial

def fatorial(x, show=False):
    """
    fatorial de um número
    :param x: o numero a ser calculado
    :param show:(opcional) mostrar ou nao a conta
    :return: o valor fatorial do n
    """

    f = 1
    for c in range(x, 0, -1):
        if show:
            print(c, end = '')
            if c>1:
                print(' x ' , end = '')
            elif c==1:
                print(' = ', end = '')
        f *= c
    return f

print(fatorial(int(input('Digite um número e veja o seu fatorial: ')), show = True))
help(fatorial)


