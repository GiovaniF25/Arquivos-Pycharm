# Crie um programa que leia notas e identifique qual a maior, menor, média e a situação do aluno:

def notas (*x, sit=True):
    global lst
    lst = [i for i in x]
    situ = 'Boa' if (sum(lst) / len(lst)) >= 7 else 'Ruim'
    dic = {'Menor nota':float(min(lst)), 'Maior nota':float(max(lst)),
           'Média': round((sum(lst) / len(lst)), 2), 'Situação':situ}
    if sit == False:
        del dic["Situação"]  # REMOVE O ITEM 'SITUAÇÃO' DO DICIONÁRIO

    print('=-'*11)
    for x, y in enumerate(dic):
        print(f'{y:-<15}  {dic[y]}')
    print('=-' *11)


notas(4, 6.25, 5, 7, 8, 9.5, 10, 9, sit=True)