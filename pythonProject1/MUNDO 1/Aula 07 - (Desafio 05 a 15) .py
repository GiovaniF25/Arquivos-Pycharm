# aprendendo sobre operações matemáticas no python
# OBS: coloquei os {:=^40} e as cores que aprendi nas aulas posteriores

print('{:=^40}'.format(' Bem vindos! '))
print('{:^40}'.format('\033[1;31m Bem vindos!\033[m '))
# se eu quero que repita 40 vezes eu faço {:^40}

n1= int(input('Um valor'))
n2= int(input('Outro valor'))
s= n1+n2
d= n1/n2
p= n1*n2

print('A soma é {}, n a divisão é {}, e o produto é {}'.format(s,d,p))
