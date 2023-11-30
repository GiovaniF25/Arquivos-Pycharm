# analise de itens de uma frase
# ESTRUTURA DE STR: (aqui eu escrevo *******UMA FRASE******* e analiso e modifico ela)

frase = 'Curso em vídeo Python'
print(frase[3]) # ele encontra a quarta letra (SEMPRE a primeira letra é o zero)
print(frase[-1]) # ele encontra a ultima letra de tras pra frente
print(frase[0:8])  # ele encontra as letras de 0 a 8
print(frase[:8]) # se nao tem nada no começo ele vai do início (0)
print(frase[8:]) # se nao tem nada no final ele vai até o fim (ultimo número)

print(frase[::-1]) # ele inverte a frase *****************IMPORTANTÍSSMO*****************

print(frase[0:8:2]) # o 2 no final significa que ele pula de 2 em 2 letras
print(frase.count('o')) # ele encontra apenas o "o" minúsculo
print(frase.upper()) # ele digita em maiúsculas
print(frase.upper().count('o'))# ele encontra apenas o "O" maiusculo

print(len(frase)) # ele conta o numero de letras com espaços da frase
print(len(frase)-frase.count(' ')) # ele conta o número de letras sem considerar espaços na frase
print(frase.replace('Python','Java')) # ele troca uma palavra por outra
print(frase.find('vídeo')) #aqui ele deixa 9 pq a palavra vídeo começa na linha 9
print(frase.split()) # aqui ele divide cada palavra e em elementos separados

f= (str(input('Digite uma frase: ')))     # aqui da pra somente escrever .split nessa linha, nao precisava ter criado uma outra em baixo
# ex: Sou de Sul Brasil
frase_separada= f.split()

print('a primeira palavra da frase é: {}'.format(frase_separada[0]))





