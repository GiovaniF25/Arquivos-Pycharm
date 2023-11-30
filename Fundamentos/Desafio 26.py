# Faça um progama que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra A
# Em que posição aparece a primeira vez
# Em que posição aparece pela ultima vez

# Frase: Amanda ama Pedro

frase=str(input('Digite uma frase: ')).lower().strip().replace('á','a').replace('ã','a').replace('à','a'). replace('â','a')
letra_a= frase.count('a')
primeira_posicao= frase.find('a')+1   # coloca +1 pq pro python começa a contagem em 0
ultima_posicao= frase.rfind('a')+1    # r find ele começa a procurar da direita pra esquerda

print('A palavra "a" aparece {} vezes, o primeiro "a" aparece na posição {}, e o ultimo "a" aparece na posição {}'. format(letra_a,primeira_posicao,ultima_posicao))