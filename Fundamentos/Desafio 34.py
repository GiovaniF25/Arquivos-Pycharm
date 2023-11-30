# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$ 1.250,00, calcule um aumento de 10%, para salário inferiores o aumento será de 15%

salario= float(input('Digite seu salário em R$: '))
if salario >= 1250:
    aumento1= float(salario*1.10)
    print('O seu novo sarlário sera de R$ {:.2f}'. format(aumento1))
else:
    aumento2 = float(salario * 1.15)
    print('O seu novo sarlário sera de R$ {:.2f}'.format(aumento2))
