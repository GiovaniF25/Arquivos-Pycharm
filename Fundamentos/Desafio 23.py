# Faça um programa que leia um número inteiro de 0 a 9999 e mostre na tela cada um dos seus dígitos separados

n =input('informe um numero')
print('Unidade:{}'.format(n[0:1]))
print('Dezena: {}'.format(n[1:2]))
print('Centena:{}'.format(n[2:3]))
print('Milhar: {}'.format(n[3:]))

# outra forma de fazer:

num = int(input('Digite um número entre 0 e 9999: '))
unidade = (num//1 % 10)
dezena = (num//10 % 10)
centena = (num//100 % 10)
milhar = (num//1000 % 10)

print('O número escolhido foi {}'. format(num))
print('A unidade é {}'. format(unidade))
print('A dezena é {}'. format(dezena))
print('A centena é {}'. format(centena))
print('A milhar é {}'. format(milhar))

#Veja os exemplos abaixo.
#Divisão: 1234 / 10 = 123,4
#Divisão inteira: 1234 //10 = 123
#Módulo: 1234 % 10 = 4
#Pra ele descobrir a centena ele faz isso:
#Faz a divisão inteira por 100: 1234 // 100 = 12
#Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
#Ou seja, a centena é 2.

#o símbolo // faz a divisão e só pega o que esta antes da vírgula.
#o símbolo % faz a divisão e só pega o que esta depois da vírgula.



