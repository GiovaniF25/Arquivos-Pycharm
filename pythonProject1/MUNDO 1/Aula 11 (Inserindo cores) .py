#cores no terminal
# ex: \033[estilo;texto;fundom
# ex: \033[1;33;43m

# primeiro para estilo (0:sem estilo);  (1:em negrito);  (4:sublinhado) e (7:inverte as configurações).
# segundo para texto (30: branco); (31: vermelho); (32:verde); (33:amarelo); (34:azul); (35:roxo) (36:ciano); (37:cinza)
# terceiro para fundo (40: branco); (41: vermelho); (42:verde); (43:amarelo); (44:azul); (45:roxo) (46:ciano); (47:cinza)


print('\033[1;31m Olá mundo,\033[m')          # se eu nao quero fundo, ou nao quero um estilo, nao coloca nada, e deixa o m sempre no final


nome = 'Giovani'
print('Olá! Muito prazer em conhece-ló {} {}'.format('\033[1;32m',nome)) # aqui a linha de baixo continua verde pq eu nao fechei a cor

print('Olá! Muito prazer em conhece-ló {} {} {} !!'.format('\033[1;32m',nome,'\033[m'))  # aqui eu coloquei mais um {} e digitei apenas '\033[m' para poder fechar a cor, ai o resto das palavras nao vao mais serem pintados

#-------------------------------------------------------------------------------------
# exemplo uso de cores:

nome = 'Giovani'
cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;30m' }

print('Olá, prazer em conhece-ló {} {} {}!!'.format(cores['amarelo'], nome, cores['limpa']))   #dentro de cores, digita se vc quer o amarelo, azul ou preto e branco