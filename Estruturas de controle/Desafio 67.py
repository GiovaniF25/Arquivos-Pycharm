# Faça um programa que mostre a tabuada de vários números, uma de cada vez
# O programa será interrempido quando o número for negativo

while True:
    numero = int(input('Digite um número inteiro para saber a sua taboada: '))
    if numero < 0:
        break
    for c in range(11):
        print(f' {c} * {numero} = {c*numero} ')

print('PROGRAMA TABOADA ENCERRADO. Volte sempre')



