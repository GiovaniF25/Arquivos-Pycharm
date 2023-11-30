# LISTAS - MUTÁVEIS
# aqui eu tenho ***** UMA LISTA**** com números ou com palavras e eu analiso e modifico ela:

lista_numeros = [5, 7, 2, 9, 4, 1, 3]  #usa isso para números

print(len(lista_numeros)) # mostra a quantidade de elementos na lista
print(max(lista_numeros)) # mostra o valor mais alto da lista
print(min(lista_numeros)) # mostra o valor mais baixo da lista
print(sum(lista_numeros)) # mostra a soma de todos os valores da lista

lista_numeros.sort() # mostra a ordem crescente da lista
print(lista_numeros)

lista_numeros.reverse() # mostra a ordem descresente da lista
print(lista_numeros)

print(sorted(lista_numeros)) # mostra a lista em ordem crescente
lista_numeros.append(15)
print(lista_numeros)   # eu posso adicionar mais elementos na lista usando isso

posicao = lista_numeros.index(max(lista_numeros)) # com o index eu acho a posição de algo que eu quero, o maior ou menos número por exemplo
print(posicao)


n1 = 'Giovani'
n2 = 'Eduarda'
n3 = 'Genésio'
lista_nomes1 = [n1, n2, n3]   # usa isso para letras, eu posso identificar quem é a variável dai colocar dentro da lista
print(len(lista_nomes1)) # mostra a quantidade de elementos na lista

#ou
lista_n1 = ['Giovani', 'Eduarda'] # ou escrever com '' as palavras
print(len(lista_n1)) # mostra a quantidade de elementos na lista
print(sorted(lista_n1)) # mostra a list em ordem alfabética

# eu posso colocar mais coisas dentro da minha lista usando o append (adicionar) mas pra isso usa o print em baixo do comando append
lista_n1.append('Genésio')
print(lista_n1) # ele deixa listado em ordem alfabética considerando a primeira letra

# eu posso colocar listas dentro de lista usando o comando (extend) mas pra isso usa o print em baixo do comando extend
lista_n1.extend(['Pedro', 'Keila', 'Jarbas','Karine'])
print(lista_n1)

# append adiciona elemento, extend adiciona lista

animais = ['gato', 'cachorro', 'vaca']
print(animais.index('cachorro'))  # aqui ele vai mostrar a posição do elemento





