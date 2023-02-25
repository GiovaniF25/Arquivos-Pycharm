# Reescreve a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade:

def numero_inteiro(numero):
    while True:
        try:
            numero = int(numero)
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: "{numero}" não é um número inteiro.\033[m')
            numero = input('Insira aqui um número inteiro: ')
        else:
            return numero

numero = numero_inteiro(input('Insira um número inteiro: '))
print(f'O numero inserido foi {numero}')

def numero_real(valor):
    while True:
        try:
            valor = float(str(valor).replace(',', '.'))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: "{valor}" não é um número real.\033[m')
            valor = input('Insira aqui um número real: ')
        else:
            return valor

real = numero_real(input('Insira aqui um número real: '))
print(f'O número real inserido foi {real}')