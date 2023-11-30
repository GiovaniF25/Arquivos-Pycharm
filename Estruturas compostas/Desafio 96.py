# Faça um programa que tenha um função chamada área, que recebe as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno

print('Controle de terreno')

def area(x,y):
    print(f'A área é do seu terreno de {x}m x {y}m é de {x*y}m²')

largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite o comprimento do terreno em metros: '))

area(largura, comprimento)

