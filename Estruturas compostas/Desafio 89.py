# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
# lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
# mostrar as notas de cada aluno individualmente


ficha_aluno = []
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Nota P1: '))
    n2 = float(input('Nota P2: '))
    media = ((n1+n2)/2)
    ficha_aluno.append([nome, [n1, n2], media] ) #eu só posso deixar entre "()" se eu tiver apenas um elemento, se eu tiver adicionando mais eu tenho que colocar em "[]"
    continuar = str(input('Quer continuar? Digite SIM ou NAO:')).upper().strip()

    if 'N' in continuar:
        break
# Mostrando as notas por ranking
print('-='*30)
print(f'{"Posição":<10}{"Nome":<10}{"Média":>8}')
print('-'*26)
for indice, aluno in enumerate(ficha_aluno):
    print(f'{indice:<10}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opcao = str(input('Deseja ver a nota de algum aluno em específico?:')).upper().strip()
    if 'S' in opcao:
        procura = int(input('Qual é a posição do aluno na lista?:'))
        print(f'as notas do aluno "{ficha_aluno[0]}" foram: {ficha_aluno[1]}')
        opcao = str(input('Deseja ver a nota de mais algum aluno em específico?:')).upper().strip()
    elif 'S' in opcao:
        procura = int(input('Qual é o indice do aluno?:'))
        print('entao, nao vou te mostar')

    elif 'N' in opcao:
        break
print('Fim')


