# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está escrito com letras maiusculas?', a.isupper())