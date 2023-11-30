# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ela ainda vai se alistar
# se é hora de se alistar
# se ja passou o prazo de alistamento
# o programa deveria mostrar o tempo que falta para se alistar

idade = int(input('Informa a sua idade: '))

if idade < 18:
    restante = (18 - idade)
    print('Ainda faltam {} anos para você se alistar'. format(restante))
elif idade == 18:
    print('Está na hora de você se alistar')
elif idade > 18:
    print('Já passou o seu prazo para alistamento')
