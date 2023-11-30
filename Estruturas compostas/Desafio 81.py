# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# -Quantos números foram digitados
# -A lista de valores, ordenada de forma decrescente
# -Se o valor 5 foi digitado e está ou não na lista


lista_num = []

while True:
    n = int(input('Digite um número: '))
    lista_num.append(n)

    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r not in 'SN':
        while r not in 'SN':
            r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if 'S' not in r:
        break

print(f'Você digitou {len(lista_num)} números no total')
lista_num.sort(reverse = True) # para colocar uma lista de trás pra frente
print(f'A lista em ordem crescente fica {lista_num}  ')

if 5 in lista_num:
    print(f'O valor 5 está na lista e apareceu {lista_num.count(5)} vezes')
else:
    print('O valor 5 não está na lista')