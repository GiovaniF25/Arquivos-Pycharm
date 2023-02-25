# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele
# foi alugado. Calcule o preço a pagar, sabendo que cada km rodado custa 15 centavos e cada dia custa 60 reais de aluguel

km = int(input('Quantos km foram rodados?'))
dias = int(input('Quantos dias o carro foi usado?'))

pago = int((km * 0.15) + (dias * 60))

print('O total a ser pago com o aluguel do carro é de R$ {:.2f}'.format(pago))