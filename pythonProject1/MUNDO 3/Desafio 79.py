# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados em ordem crescente

lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Esse número já está inserido na lista')

    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break

print(sorted(lista))