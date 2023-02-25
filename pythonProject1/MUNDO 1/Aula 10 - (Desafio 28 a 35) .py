# início do uso do if e else:

nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'GIOVANI':
    print('Que nome lindo')
else:
    print('Seu nome é tão feio!')
print('Bom dia {}!'.format(nome))

# eu posso ter apenas if e elif, sem ter else


# ---------------------------------------------------------------------------------------------------
# Exemplos de uso de if e else

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1+n2)/2
print('A sua média foi {:.1f}'.format(n))

if n>=7.0:
    print('Você tirou uma nota boa!')
else:
    print('Estude mais, seu burro!')

# ---------------------------------------------------------------------------------------------------
# outro exemplo, pra nao escrever os intervalos, <= ou >=, ao inves de usar o elif, usa else if, ex:

idade= int(input("Digite a idade da pessoa: "))


if idade <=1:
    print("Recém nascido")
else:
    if idade < 13:
        print("Criança")
    else:
        if idade < 18:
            print ("Adolescente")
        else:
            if idade < 60:
                print ("Adulto")
            else:
                if idade < 80:
                    print ("Idoso")
                else:
                    print ("Longevo")


print ("Acabou.")