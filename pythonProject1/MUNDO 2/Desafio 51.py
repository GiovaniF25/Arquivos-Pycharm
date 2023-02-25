# Desenvolva um programa que leia o primeiro termo e a razão de uma PA e sua razão. No final mostre os 10 primeiros termons

primeiro_termo = int(input('Digite o primeiro termo escolhido: '))
razao = int(input('Digite a razão escolhida: '))
ultimo_termo = primeiro_termo + (10-1)*razao

for c in range(primeiro_termo, ultimo_termo+1, razao):
    print('{}'.format(c), end = ' ')

