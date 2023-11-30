# Crie um programa que leia o ano de nascimento de 7 pessoas, e no final mostre quantas pessoas
# atingiram a maior idade e quantas são menores

contagem = 0

for c in range(1, 8):
    ano = int(input('O ano de nascimento da {}° é: '.format(c)))
    if ano >= 2002:
        contagem += 1

print('Das 7 pessoas analisadas, {} já é (são) maiores de idade e {} ainda é(são) menores de idade'.format(contagem,c-contagem))


# ou usar uma importação de biblioteca
from datetime import date
date.today().year

menores = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - pessoa < 18:
        menores += 1
print('\n{} são Maiores e {} são menores.'.format(7 - menores, menores))


