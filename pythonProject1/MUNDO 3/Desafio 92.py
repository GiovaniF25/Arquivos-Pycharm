# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) num dicionário se por acaso o CTPS for diferente de zero, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

cadastro = {}

cadastro['Nome'] = str(input("Nome: "))
ano = int(input("Ano de Nascimento: "))
cadastro['Idade'] = datetime.now().year - ano
cadastro['N° CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro['N° CTPS'] != 0:
    cadastro["Contratação"] = int(input("Ano de Contratação: "))
    cadastro["Salário"] = int(input("Salário: R$ "))
    cadastro['Aposentadoria'] = cadastro["Contratação"] + 35 - ano

print('..'*30)
for k, v in cadastro.items():
    print(f'    - {k}:{v}')