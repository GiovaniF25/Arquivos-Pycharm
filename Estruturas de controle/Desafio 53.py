# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconidere os espaços

frase = input('Digite uma frase').upper().strip()
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")