# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quandos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode excedere 30% do salário para o emprestimo nao ser negado

valor = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário: '))
tempo = int(input('Digite quanto tempo em meses que você vai demorar para pagar: '))

print('O valor do seu salário é de R$ {}, o valor da casa é de R$ {} e você vai demorar {} meses para pagar'.format(salario, valor, tempo))

prestacao = int((valor)/(salario*0.3))
print(prestacao)

if prestacao > tempo:
    print('Seu empréstimo foi negado, são necessário {} parcelas para efetuar o empréstimo'. format(prestacao))
else:
    print('Seu empréstimo foi aceito')

