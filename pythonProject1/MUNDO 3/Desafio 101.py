# Crie um programa que vai receber uma função chamada voto() que vai receber como parametro o ano de nascimento
# de uma pessoa, retornado um valor literal, indicando se uma pessoa tem o voto NEGADO, OPCIONAL OU OBRIGATÓRIO

# Se eu for resolver sem o RETURN fica assim
def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        print(f' {idade} anos, não vota')
    elif 16 <= idade < 65:
        print(f' {idade} anos, voto opcional')
    else:
        print(f' {idade} anos, Voto obrigatório')

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
voto(ano_nascimento)

# Resolvendo com return, fica assim:
def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade <16:
        return f' {idade} anos, não vota'
    elif 16 <= idade < 65:
        return f' {idade} anos, voto opcional'
    else:
        return f' {idade} anos, Voto obrigatório'

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
print(voto(ano_nascimento))

#basicamente eu só não deixo o print dentro e começo a deixar ele fora e escrevo o return

