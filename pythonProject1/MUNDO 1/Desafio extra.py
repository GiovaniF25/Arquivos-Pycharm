from random import choice
import sys

lista = ['abelha', 'macaco', 'cachorro']
palavra_secreta1 = choice(lista)

print('Vamos brincar, Eduarda? Adivinhe o animal em que eu estou pensando! ')
pergunta_1 = str(input('Você vai querer um dica? digite sim ou não: ')).lower().strip()
if pergunta_1 == 'sim':
    print('OK, vou ter dar uma dica para você tentar adivinhar a palavra em que eu estou pensando')

    if  pergunta_1 == 'sim' and palavra_secreta1 == 'macaco':
        dica = ' Evolução humana '
        print('{}'.format(dica))

        t1 = str(input('Digite o nome do animal que você está pensando: '))

        if  t1 == palavra_secreta1:
            print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')

        elif t1 != palavra_secreta1:
            print('Que pena, você errou!')
            print('Game over, a palavra era {}'.format(palavra_secreta1))
            sys.exit()

    if  pergunta_1 == 'sim' and palavra_secreta1 == 'abelha':
        dica = ' Amarela e preta '
        print('{}'.format(dica))

        t1 = str(input('Digite o nome do animal que você está pensando: '))

        if  t1 == palavra_secreta1:
            print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')

        elif t1 != palavra_secreta1:
            print('Que pena, você errou!')
            print('Game over, a palavra era {}'.format(palavra_secreta1))
            sys.exit()

    if pergunta_1 == 'sim' and palavra_secreta1 == 'cachorro':
        dica = ' Melhor amigo do homem:'
        print('{}'.format(dica))

        t1 = str(input('Digite o nome do animal que você está pensando: '))

        if t1 == palavra_secreta1:
            print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')

        elif t1 != palavra_secreta1:
            print('Que pena, você errou!')
            print('Game over, a palavra era {}'.format(palavra_secreta1))
            sys.exit()
else:
    print('OK, como você não quer uma dica, então vou te dar 3 tentativas para adivinhar a palavra que eu estou pensando')
    t1 = str(input('Digite a primeira tentativa: '))

    if  t1 == palavra_secreta1:
        print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')
    elif t1 != palavra_secreta1:
        print('Que pena, você errou')

        t2 = str(input('Digite a segunda tentativa: '))
        if   t2 == palavra_secreta1:
            print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')
        elif t2 != palavra_secreta1:
            print('Que pena, você errou')

            t3 = str(input('Digite a terceira tentativa: '))
            if t3 == palavra_secreta1:
                print('Parabéns, você acertou na primeira tentativa, agora escolha o seu prêmio!')
            elif t3 != palavra_secreta1:
                print('Que pena, você errou')

            print('Game over, a palavra era {}'. format(palavra_secreta1))
            sys.exit()









