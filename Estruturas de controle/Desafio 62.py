# Melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos
# O programa encerra quando ele disse que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo escolhido: '))
razao = int(input('Digite a razão escolhida: '))

pa = primeiro_termo
contador = 1
continuar = 0
total = 0
continuar = 10
print('A progessão artimética de {} é: '.format(primeiro_termo))
while continuar != 0:
    total = total + continuar
    while contador <= total:
        print('{}'.format(pa), end = ' ')
        pa = pa + razao
        contador = contador + 1
    print(' ')
    print('Pausa')
    continuar = int(input('Quantos termos a mais você quer mostrar?: '))

