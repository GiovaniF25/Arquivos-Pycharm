# Desenvola um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens até 200Km, e R$ 0,45 para viagens mais longas

distancia= float(input('Qual é a distância da sua viagem em km?: '))
if distancia <= 200:
    v1= float(distancia*0.50)
    print('O custo de sua viagem será R${:.2f}'. format(v1))
else:
    v2 = float(distancia*0.45)
    print('O custo de sua viagem será R${:.2f}'.format(v2))