#retorno de valores


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
somar(2,2,5)
somar(3,3)
somar(4)
# no print vai aparecer isso:
#A soma vale 9
#A soma vale 6
#A soma vale 4

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

resposta1 = somar(2,2,5)
resposta2 = somar(3,3)
resposta3 =somar(4)
print(f'As somas valem {resposta1} {resposta2} e {resposta3}')
# no print vai aparecer isso:
# As somas valem 9 6 e 4

# ele nao vai repetir toda a vez, a soma vale..., ele vai fazer uma vez só

#exercício:

def fatorial(num):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f
# aqui eu criei uma função fatorial, essa eu mesmo podia importar, mas a ideia dos def é vc criar funcoes como voce quiser

num = int(input('Digite um número: '))
f1 = fatorial(num)
f2 = fatorial(4)

print(f'O fatorial de {num} é igual a {f1}, {f2} ')