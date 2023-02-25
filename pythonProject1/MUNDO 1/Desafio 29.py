# Escreve um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre um mensagem dizendo que
# ele foi multado. A multa vai custar R$ 7.00 por cada km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Você não foi multado!')
else:
    multa=(velocidade - 80)*7
    print('Você foi multado e pagará R$ {:.1f}'.format(multa))