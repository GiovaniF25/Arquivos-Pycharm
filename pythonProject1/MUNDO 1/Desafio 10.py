# Crie um programa que leia qual é o saldo de uma pessoa e converta-o para dolares ($1 = R$3.27)

r = int(input('Quantos reais você tem em sua carteira? '))
c= (r/3.27)

print('Com R$ {:2f}, você pode comprar $ {:.2f}'. format(r,c))
