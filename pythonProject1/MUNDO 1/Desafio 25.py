# Crie um programa que leia o nome de uma pessoa e verifique se existe a palavra "Silva" em seu nome

nome= str((input('Digite o seu nome: '))).strip().upper().split()     # strip pra ele desconsiderar os espaços, upper pra transformar em maiusculo
print('Seu nome tem Silva? {}'.format('SILVA ' in nome))              # (pois na linha de baixo eu escrevi SILVA, se fosse lower, eu escreveria silva em baixo
                                                                      # split é pra dividir as palavras
                                                                      # deixa um espaço depois de silva pq se tiver um silvana ele irá contar tbm se eu nao fizer isso