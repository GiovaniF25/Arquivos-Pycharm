# a Condefederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua cateogira
# até 9 anos - mirim
# até 14 anos - infantil
# até 19 anos - junior

idade = int(input('Informe a sua idade: '))

if idade < 9:
    print('Vc é mirim')
elif idade >= 9 and idade < 14:
    print('Vc é infantil')
elif idade < 19:
    print('Vc é junior')
