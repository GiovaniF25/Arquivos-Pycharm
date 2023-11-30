# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calculando o seu IMC e mostre se:
# abaixo de 18,5: abaixo do peso
# entre 18,5 e 25: peso ideal
# de 25 até 30: sobrepeso
# acima de 40: baleia assassina

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura:'))
imc = (peso)/(altura**2)

if imc < 18.5:
    print('Abaixo do peso, raquitico')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 35:
    print('Sobrepeso')
elif imc > 40:
    print('Se ajude!!!')