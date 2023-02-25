# introdução do uso do elif junto com o if e o else:

nome = str(input('Qual é o seu nome?: ')).lower()
if nome == 'giovani':
    print('Que nome bonito!')
elif nome == 'joão' or nome == 'maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana claudia jéssica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem feio')

print('Tenha um bom dia {}'.format(nome))