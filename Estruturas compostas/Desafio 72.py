# Crie um programa que tem um TUPLA totalmente preenchida com uma contagem por extenso, de 0 a 10
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso


cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Digite novamente', end= ' ')
print(f'Você digitou o número {cont[n]}') # se no lugar do n eu colocasse 0, ele iria me mostrar o 0, mas como eu quero mostrar o número que o programa receberu, eu coloco o N

while True:
    continuar = str(input('Você quer continuar digitando números? [S/N]: ')).upper().strip()[0]
    if continuar in 'S':
        while True:
            n = int(input('Digite outro número entre 0 e 10: '))
            if 0 <= n <= 10:
                break
    if continuar in 'N':
        break
print('Fim do processo')