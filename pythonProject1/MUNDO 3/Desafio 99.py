# Faça um programa que tenha um função maior(), que receba vários parametros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(*num):
    contador = 0
    maior = 0
    print('\nAnalisando os valores: ')
    for valor in num:
        print(f'{valor}', end =' ')
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f' Foram informados {contador} valores e o maior valor informado foi {maior}')

maior(2,9,4,5,7,1)
maior(2,9,4)
maior(6)