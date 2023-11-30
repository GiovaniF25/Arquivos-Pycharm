# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

nome_cidade = str(input('Digite o nome de sua cidade: ')).strip()  # o strip elimina os espaços
print(nome_cidade[0:5].upper() == 'SANTO') # santo tem 5 letras e deixei o upper pra nao ter perigo do cliente escreve Santo ou santo