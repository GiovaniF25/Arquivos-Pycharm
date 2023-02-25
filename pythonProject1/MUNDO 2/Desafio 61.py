# Refaça o exercício 51 lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros termos da progresão
# usando o while


primeiro_termo = int(input('Digite o primeiro termo escolhido: '))
razao = int(input('Digite a razão escolhida: '))
print('A progessão artimética de {} é: '.format(primeiro_termo))

contador = 1

while contador <= 10:
    print('{}'.format(primeiro_termo), end = ' ')
    primeiro_termo = primeiro_termo + razao
    contador = contador + 1
print(' ')
print('Fim')
