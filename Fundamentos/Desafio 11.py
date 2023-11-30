# Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade de
# tinta que precisa para pinta-lá. (1 lata de tinta pinta 2m²)

largura=float(input('digite a largura da parede '))
altura=float(input('digite a altura da parede '))
área= largura*altura
tinta=largura*altura/2
print('A quantidade de latas de tinta necessárias para pintar essa parede, sabendo que cada lata de tinta pinta 2m² é de {}l'. format(tinta))

