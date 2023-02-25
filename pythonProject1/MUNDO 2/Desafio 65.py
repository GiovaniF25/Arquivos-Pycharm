# Crie um programa que leia vários números inteiros pelo teclado. No final da execução
# mostre a média entre todos os valores e qual foi o maior e o menores valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores


lista_numero = []
contador = 0

while True:
    numero = int(input('Digite um número: '))
    resposta = str(input("Quer continuar? Sim ou não?: ")).upper().strip()[0]
    lista_numero.append(numero)
    contador += 1
    if resposta not in 'N':
        break


print('Você digitou {} números'. format(contador))
print('A média dos números digitados foi {}'. format((sum(lista_numero)/len(lista_numero))))
print('O maior número digitado foi {}'.format(max(lista_numero)))
print('O menor número digitado foi {}'.format(min(lista_numero)))

