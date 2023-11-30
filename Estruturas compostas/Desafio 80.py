# Crie um programa onde o usuário possa digitar cinco valores numpericos e cadastre-os em uma lista,
# já na posição correta e em ordem

lista =[]

for c in range(5):
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('Adicionando o valor a lista')

print(f' Os valores digitados em ordem foram: {sorted(lista)}')

# ou
lista.sort()
print(f' Os valores digitados em ordem foram: {lista}')