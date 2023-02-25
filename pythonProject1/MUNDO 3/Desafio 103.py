# Faça um programa que tenha uma função que recebe dois parametros opcionais mostrando o nome o númeor de gols do jogador

# solução simples
def ficha(nome, gols):
    return f'O Jogador: {nome}, fez {gols} gol(s) no campeonato.'

print(ficha(str(input('Nome do Jogador: ')), str(input('Número de Gols: '))))

# se eu fizer dessa forma eu posso consigo formatar e deixar o nome e numero de gols vazios e o programa funcionar igual
# diferentemente de eu deixar o nome o numero de gols vazios no programa de cima, esse nao iria rodar

def ficha(nome, gols):
    if nome == '':
        nome = f'\033[33m {"<Desconhecido>"} \033[m'
    if gols == '':
        gols = f'\033[33m {"0"} \033[m'

    return f'O Jogador: {nome}, fez {gols} gol(s) no campeonato.'

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
print(ficha(nome, gols))